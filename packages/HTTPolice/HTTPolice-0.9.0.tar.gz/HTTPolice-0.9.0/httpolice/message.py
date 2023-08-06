import codecs
from datetime import datetime, timedelta
from email import message_from_bytes as parse_email_message
import email.errors
import json
from urllib.parse import parse_qs
import xml.etree.ElementTree

from bitstring import Bits
import defusedxml
import defusedxml.ElementTree

from httpolice import known
from httpolice.blackboard import Blackboard, derived_property
from httpolice.codings import decode_brotli, decode_deflate, decode_gzip
from httpolice.header import HeadersView
from httpolice.known import cc, h, media, st, tc, upgrade, warn
from httpolice.parse import parse
from httpolice.structure import (FieldName, HeaderEntry, HTTPVersion,
                                 Unavailable, http2, http11, okay)
from httpolice.syntax import rfc7230
from httpolice.util.data import iterbytes
from httpolice.util.text import force_unicode, format_chars, printable


# This list is taken from the HTML specification --
# https://www.w3.org/TR/html/sec-forms.html#urlencoded-form-data --
# as the exhaustive list of bytes that can be output
# by a "conformant" URL encoder.

URL_ENCODED_GOOD_CHARS = Bits(
    1 if (x in [0x25, 0x26, 0x2A, 0x2B, 0x2D, 0x2E, 0x5F] or
          0x30 <= x < 0x40 or 0x41 <= x < 0x5B or 0x61 <= x < 0x7B) else 0
    for x in range(256)
)


class Message(Blackboard):

    """An HTTP message (request or response)."""

    self_name = u'msg'

    def __init__(self, version, header_entries, body, trailer_entries=None,
                 remark=None):
        super(Message, self).__init__()
        self.version = (HTTPVersion(force_unicode(version))
                        if version is not None else None)
        self.header_entries = [HeaderEntry(k, v)
                               for k, v in header_entries]
        self.body = bytes(body) if okay(body) else body
        self.trailer_entries = [HeaderEntry(k, v)
                                for k, v in trailer_entries or []]
        self.rebuild_headers()
        self.annotations = {}
        self.remark = remark

    @property
    def annotated_header_entries(self):
        return [(entry, self.annotations.get((False, i), [entry.value]))
                for i, entry in enumerate(self.header_entries)]

    @property
    def annotated_trailer_entries(self):
        return [(entry, self.annotations.get((True, i), [entry.value]))
                for i, entry in enumerate(self.trailer_entries)]

    def rebuild_headers(self):
        self.headers = HeadersView(self)

    @derived_property
    def decoded_body(self):
        """The payload body with Content-Encoding removed."""
        r = self.body
        codings = self.headers.content_encoding.value[:]
        while codings and okay(r) and r:
            coding = codings.pop()
            decoder = {cc.gzip: decode_gzip,
                       cc.x_gzip: decode_gzip,
                       cc.deflate: decode_deflate,
                       cc.br: decode_brotli}.get(coding)
            if decoder is not None:
                try:
                    r = decoder(r)
                except Exception as e:
                    self.complain(1037, coding=coding, error=e)
                    r = Unavailable(r)
            elif okay(coding):
                self.complain(1036, coding=coding)
                r = Unavailable(r)
            else:
                r = Unavailable(r)
        return r

    @derived_property
    def guessed_charset(self):
        charset = 'utf-8'
        if self.headers.content_type.is_okay:
            charset = self.headers.content_type.param.get(u'charset', charset)

        try:
            codec = codecs.lookup(charset)
        except (LookupError, UnicodeError):
            return None
        charset = codec.name

        if okay(self.decoded_body):
            try:
                self.decoded_body.decode(charset)   # pylint: disable=no-member
            except UnicodeError:
                return None
        return charset

    @derived_property
    def unicode_body(self):
        if not okay(self.decoded_body):
            return self.decoded_body
        if not okay(self.guessed_charset):
            return Unavailable(self.decoded_body)
        # pylint: disable=no-member
        return self.decoded_body.decode(self.guessed_charset)

    @derived_property
    def content_is_full(self):
        """Does this message carry a complete instance of its Content-Type?"""
        return True

    @derived_property
    def json_data(self):
        if self.headers.content_type.is_okay and \
                known.media_type.is_json(self.headers.content_type.item) and \
                okay(self.unicode_body) and self.content_is_full:
            try:
                r = json.loads(self.unicode_body)
            except ValueError as e:
                self.complain(1038, error=e)
                r = Unavailable(self.unicode_body)
            else:
                if self.guessed_charset not in ['ascii', 'utf-8', None]:
                    self.complain(1281)
            return r
        return None

    @derived_property
    def xml_data(self):
        if self.headers.content_type.is_okay and \
                known.media_type.is_xml(self.headers.content_type.item) and \
                okay(self.decoded_body) and self.content_is_full:
            try:
                # It's not inconceivable that a message might contain
                # maliciously constructed XML data, so we use `defusedxml`.
                return defusedxml.ElementTree.fromstring(self.decoded_body)
            except defusedxml.EntitiesForbidden:
                self.complain(1275)
                return Unavailable(self.decoded_body)
            # https://bugs.python.org/issue29896
            except (xml.etree.ElementTree.ParseError, UnicodeError) as e:
                self.complain(1039, error=e)
                return Unavailable(self.decoded_body)
        else:
            return None

    @derived_property
    def multipart_data(self):
        ctype = self.headers.content_type
        if ctype.is_okay and \
                known.media_type.is_multipart(ctype.value.item) and \
                okay(self.decoded_body) and self.content_is_full:
            # All multipart media types obey the same general syntax
            # specified in RFC 2046 Section 5.1,
            # and should be parseable as email message payloads.
            multipart_code = (b'Content-Type: ' + ctype.entries[0].value +
                              b'\r\n\r\n' + self.decoded_body)
            parsed = parse_email_message(multipart_code)
            for d in parsed.defects:
                if isinstance(d, email.errors.NoBoundaryInMultipartDefect):
                    self.complain(1139)
                elif isinstance(d, email.errors.StartBoundaryNotFoundDefect):
                    self.complain(1140)
            if not parsed.is_multipart():
                return Unavailable(self.decoded_body)
            return parsed
        return None

    @derived_property
    def url_encoded_data(self):
        if self.headers.content_type == \
                media.application_x_www_form_urlencoded and \
                okay(self.decoded_body) and self.content_is_full:
            for char in iterbytes(self.decoded_body):
                if not URL_ENCODED_GOOD_CHARS[ord(char)]:
                    self.complain(1040, char=format_chars([char]))
                    return Unavailable(self.decoded_body)
            # pylint: disable=no-member
            return parse_qs(self.decoded_body.decode('ascii'))
        return None

    @derived_property
    def displayable_body(self):
        """
        The payload body in a form that is appropriate for display in a message
        preview, along with a list of phrases explaining which transformations
        have been applied to arrive at that form.
        """
        removing_te = [u'removing Transfer-Encoding'] \
            if self.headers.transfer_encoding else []
        removing_ce = [u'removing Content-Encoding'] \
            if self.headers.content_encoding else []
        decoding_charset = [u'decoding from %s' % self.guessed_charset] \
            if self.guessed_charset and self.guessed_charset != 'utf-8' else []
        pretty_printing = [u'pretty-printing']

        if okay(self.json_data):
            r = json.dumps(self.json_data, indent=2, ensure_ascii=False)
            transforms = \
                removing_te + removing_ce + decoding_charset + pretty_printing
        elif okay(self.unicode_body):
            r = self.unicode_body
            transforms = removing_te + removing_ce + decoding_charset
        elif okay(self.decoded_body):
            # pylint: disable=no-member
            r = self.decoded_body.decode('utf-8', 'replace')
            transforms = removing_te + removing_ce
        elif okay(self.body):
            r = self.body.decode('utf-8', 'replace')
            transforms = removing_te
        else:
            return self.body, []

        limit = 1000
        if len(r) > limit:
            r = r[:limit]
            transforms += [u'taking the first %d characters' % limit]

        pr = printable(r)
        if r != pr:
            r = pr
            transforms += [u'replacing non-printable characters '
                           u'with the \ufffd sign']

        return r, transforms

    @derived_property
    def transformed_by_proxy(self):
        if warn.transformation_applied in self.headers.warning:
            self.complain(1189)
            return True
        return None

    @derived_property
    def is_tls(self):
        raise NotImplementedError()


def check_message(msg):
    """Run all checks that apply to any message (both request and response)."""
    complain = msg.complain
    version = msg.version
    headers = msg.headers

    x_prefixed = []
    for hdr in headers:
        # Check the header name syntax.
        parse(hdr.name, rfc7230.field_name, complain, 1293, header=hdr,
              place=u'field name')
        # Force parsing every header present in the message
        # according to its syntax rules.
        _ = hdr.value
        if known.header.is_deprecated(hdr.name):
            complain(1197, header=hdr)
        if hdr.name.startswith(u'X-') and hdr.name not in known.header:
            x_prefixed.append(hdr)
    if x_prefixed:
        complain(1277, headers=x_prefixed)

    # Force checking the payload according to various rules.
    _ = msg.decoded_body
    _ = msg.unicode_body
    _ = msg.json_data
    _ = msg.xml_data
    _ = msg.multipart_data
    _ = msg.url_encoded_data

    if version == http11 and headers.trailer.is_present and \
            tc.chunked not in headers.transfer_encoding:
        # HTTP/2 supports trailers but has no notion of "chunked".
        complain(1054)

    for entry in msg.trailer_entries:
        if entry.name not in headers.trailer:
            complain(1030, header=entry)

    if headers.transfer_encoding.is_present and \
            headers.content_length.is_present:
        complain(1020)

    for opt in headers.connection:
        if known.header.is_bad_for_connection(FieldName(opt)):
            complain(1034, header=headers[FieldName(opt)])

    if headers.content_type.is_okay:
        if known.media_type.is_deprecated(headers.content_type.item):
            complain(1035)
        for dupe in headers.content_type.param.duplicates():
            complain(1042, param=dupe)

    if headers.content_type == media.application_json and \
            u'charset' in headers.content_type.param:
        complain(1280, header=headers.content_type)

    if headers.date > datetime.utcnow() + timedelta(seconds=10):
        complain(1109)

    for warning in headers.warning:
        if warning.code < 100 or warning.code > 299:
            complain(1163, code=warning.code)
        if okay(warning.date) and headers.date != warning.date:
            complain(1164, code=warning.code)

    for pragma in headers.pragma:
        if pragma != u'no-cache':
            complain(1160, pragma=pragma.item)

    for protocol in headers.upgrade:
        if protocol.item == u'h2':
            complain(1228)
        if protocol.item == upgrade.h2c and msg.is_tls:
            complain(1233)

    if getattr(msg, 'status', None) == st.early_hints:
        # 103 (Early Hints) responses are weird in that the headers they carry
        # do not apply to themselves (RFC 8297 Section 2) but only to the final
        # response (and then only speculatively). For such responses, we limit
        # ourselves to checks that do not rely on having a complete and
        # self-consistent message header block.
        return

    if headers.upgrade.is_present and u'upgrade' not in headers.connection:
        complain(1050)

    if msg.transformed_by_proxy:
        if warn.transformation_applied not in headers.warning:
            complain(1191)
        if headers.cache_control.no_transform:
            complain(1192)

    if version == http2:
        for hdr in headers:
            if hdr.name in [h.connection, h.transfer_encoding, h.keep_alive]:
                complain(1244, header=hdr)
            elif hdr.name == h.upgrade:
                complain(1245)
