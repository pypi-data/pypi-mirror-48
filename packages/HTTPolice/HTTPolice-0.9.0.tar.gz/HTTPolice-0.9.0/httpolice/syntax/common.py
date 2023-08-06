from httpolice.citation import RFC
from httpolice.known import media
from httpolice.parse import auto, can_complain, fill_names, octet, octet_range
from httpolice.structure import MediaType


ALPHA = octet_range(0x41, 0x5A) | octet_range(0x61, 0x7A)               > auto
CHAR = octet_range(0x01, 0x7F)                                          > auto
CTL = octet_range(0x00, 0x1F) | octet(0x7F)                             > auto
DIGIT = octet_range(0x30, 0x39)                                         > auto
DQUOTE = octet(0x22)                                                    > auto
HEXDIG = DIGIT | 'A' | 'B' | 'C' | 'D' | 'E' | 'F'                      > auto
HTAB = octet(0x09)                                                      > auto
SP = octet(0x20)                                                        > auto
VCHAR = octet_range(0x21, 0x7E)                                         > auto


_BAD_MEDIA_TYPES = {
    MediaType(u'application/text'): media.text_plain,
    MediaType(u'plain/text'): media.text_plain,
    MediaType(u'text/json'): media.application_json,
}

@can_complain
def check_media_type(complain, mtype):
    if mtype in _BAD_MEDIA_TYPES:
        complain(1282, bad=mtype, good=_BAD_MEDIA_TYPES[mtype])
    return mtype


fill_names(globals(), RFC(5234))
