History of changes
==================


0.9.0 - 2019-06-27
~~~~~~~~~~~~~~~~~~

Added
-----
- Basic checks for most of the headers defined by `WHATWG Fetch`_,
  such as ``Access-Control-Allow-Origin``.
- Updated workarounds for HAR files exported from Chrome and Firefox.
  More checks are now skipped on such files, which means
  fewer false positives due to missing or mangled data.
- Notice `1282`_ is now reported on ``application/text``.

Fixed
-----
- Notice `1276`_ is now a comment, not an error.
- Notice `1277`_ is no longer reported on ``X-Real-IP``.
- Notice `1029`_ (``TE`` requires ``Connection: TE``)
  is now only reported on HTTP/1.1 requests.

.. _WHATWG Fetch: https://fetch.spec.whatwg.org/
.. _1029: https://httpolice.readthedocs.io/page/notices.html#1029


0.8.0 - 2019-03-03
~~~~~~~~~~~~~~~~~~
- Dropped Python 2 support. If you need it, use the older versions.
- HTTPolice no longer requires `six`_ nor `singledispatch`_.
- HTTPolice now pulls in `Google’s Brotli`_ instead of `brotlipy`_,
  but this is merely a packaging change; it can work with either.
- Notices `1299`_ and `1300`_ are no longer reported on ``Alt-Svc``.

.. _six: https://pypi.org/project/six/
.. _singledispatch: https://pypi.org/project/singledispatch/
.. _Google’s Brotli: https://pypi.org/project/Brotli/
.. _brotlipy: https://pypi.org/project/brotlipy/


0.7.0 - 2018-03-31
~~~~~~~~~~~~~~~~~~

Changed
-------
- Reflecting changes in `RFC 8187`_ and `RFC 8259`_,
  notices `1253`_ (bad charset) and `1281`_ (bad encoding for JSON)
  are now reported for all encodings other than UTF-8, and
  notice 1255 (ISO-8859-1 in Content-Disposition) has been removed.

.. _RFC 8259: https://tools.ietf.org/html/rfc8259
.. _RFC 8187: https://tools.ietf.org/html/rfc8187
.. _1253: https://httpolice.readthedocs.io/page/notices.html#1253

Added
-----
- Checks for quoted commas and semicolons that might confuse a naive parser
  (notices `1299`_, `1300`_).
- New checks for Link headers according to `RFC 8288`_ (notices `1307`_,
  `1308`_, `1309`_).
- Checks for `immutable responses`_ (notices `1301`_, `1302`_, `1303`_).
- `Early hints`_ are now recognized (due to their idiosyncratic semantics,
  they avoid many checks that are applied to all other responses).
- Checks for the `Accept-Post`_ header (notice `1310`_).
- Check for no Transfer-Encoding in response to HTTP/1.0 (notice `1306`_).
- Check for 100 (Continue) before switching protocols (notice `1305`_).
- Check that the sequence of responses to a request makes sense
  (notice `1304`_).
- HAR files exported from Chrome and `Insomnia`_ are handled slightly better.

.. _1299: https://httpolice.readthedocs.io/page/notices.html#1299
.. _1300: https://httpolice.readthedocs.io/page/notices.html#1300
.. _1301: https://httpolice.readthedocs.io/page/notices.html#1301
.. _1302: https://httpolice.readthedocs.io/page/notices.html#1302
.. _1303: https://httpolice.readthedocs.io/page/notices.html#1303
.. _1304: https://httpolice.readthedocs.io/page/notices.html#1304
.. _1305: https://httpolice.readthedocs.io/page/notices.html#1305
.. _1306: https://httpolice.readthedocs.io/page/notices.html#1306
.. _1307: https://httpolice.readthedocs.io/page/notices.html#1307
.. _1308: https://httpolice.readthedocs.io/page/notices.html#1308
.. _1309: https://httpolice.readthedocs.io/page/notices.html#1309
.. _1310: https://httpolice.readthedocs.io/page/notices.html#1310
.. _RFC 8288: https://tools.ietf.org/html/rfc8288
.. _immutable responses: https://tools.ietf.org/html/rfc8246
.. _Early hints: https://tools.ietf.org/html/rfc8297
.. _Accept-Post: https://www.w3.org/TR/ldp/#header-accept-post
.. _Insomnia: https://insomnia.rest/

Fixed
-----
- Headers like `Allow`_ and `Accept`_ are now parsed more correctly
  (`RFC Errata 5257`_).
- ``gzip``-encoded payloads are now decompressed more reliably.
- When `analyzing TCP streams`_, HTTPolice now uses a stricter heuristic
  for detecting HTTP/1.x streams, producing fewer spurious `1006`_/`1009`_
  notices.
- Notice `1291`_ (Preference-Applied needs Vary) is no longer reported
  on responses to POST.

.. _Allow: https://tools.ietf.org/html/rfc7231#section-7.4.1
.. _Accept: https://tools.ietf.org/html/rfc7231#section-5.3.2
.. _RFC Errata 5257: https://www.rfc-editor.org/errata/eid5257


0.6.0 - 2017-08-02
~~~~~~~~~~~~~~~~~~

Changed
-------
- Notice `1277`_ (obsolete 'X-' prefix) is now reported only once per message.
- When parsing TCP streams, HTTPolice no longer attempts to process very long
  header lines (currently 16K; they will fail with notice `1006`_/`1009`_)	
  and message bodies (currently 1G; notice `1298`_).
- Notice 1259 (malformed parameter in Alt-Svc) has been removed: the same
  problem is now reported as notice `1158`_.
- The syntax of `chunk extensions`_ is no longer checked.

Added
-----
- Checks for the `Forwarded`_ header (notices `1296`_, `1297`_).

Fixed
-----
- Fixed a few bugs and design problems that caused HTTPolice to use more time
  and memory than necessary in various cases (sometimes much more).
- Fixed some Unicode errors under Python 2.
- Notice `1013`_ is no longer wrongly reported for some headers
  such as Vary.
- Fixed a crash on some pathological values of 'charset' in Content-Type.

.. _Forwarded: https://tools.ietf.org/html/rfc7239
.. _chunk extensions: https://tools.ietf.org/html/rfc7230#section-4.1.1
.. _1009: https://httpolice.readthedocs.io/page/notices.html#1009
.. _1298: https://httpolice.readthedocs.io/page/notices.html#1298
.. _1158: https://httpolice.readthedocs.io/page/notices.html#1158
.. _1296: https://httpolice.readthedocs.io/page/notices.html#1296
.. _1297: https://httpolice.readthedocs.io/page/notices.html#1297
.. _1013: https://httpolice.readthedocs.io/page/notices.html#1013


0.5.2 - 2017-03-24
~~~~~~~~~~~~~~~~~~
- Fixed a few rare crashing bugs found with `american fuzzy lop`_.
- Fixed a couple cosmetic bugs in HTML reports.
- When parsing a message with an unknown `transfer coding`_, HTTPolice now
  correctly skips any checks on its payload body (such as notice `1038`_).

.. _american fuzzy lop: http://lcamtuf.coredump.cx/afl/
.. _transfer coding: https://tools.ietf.org/html/rfc7230#section-4


0.5.1 - 2017-03-15
~~~~~~~~~~~~~~~~~~
- Fixed compatibility with `httpolice-devtool`_ (when you point it to a local
  `hpoliced`_ instance).

.. _httpolice-devtool:
   https://chrome.google.com/webstore/detail/httpolice-devtool/hnlnhebgfcfemjaphgbeokdnfpgbnhgn
.. _hpoliced: https://pypi.org/project/hpoliced/


0.5.0 - 2017-03-12
~~~~~~~~~~~~~~~~~~

Added
-----
- When `analyzing TCP streams`_, HTTPolice now reorders exchanges
  based on the Date header. In other words, messages sent at the same time
  on different connections are now close to each other in the report.
- Checks for the `Prefer`_ mechanism (notices `1285`_ through `1291`_).
- The syntax of method and header names and reason phrases is now checked
  for all messages, not only for those parsed from TCP streams
  (notices `1292`_, `1293`_, `1294`_).
- Check for method names that are not uppercase (notice `1295`_).
- The XML-related features removed in 0.4.0 have been restored.
- Check for cacheable 421 (Misdirected Request) responses (notice `1283`_).
- Check for 202 (Accepted) responses with no body (notice `1284`_).
- HTML reports have been optimized to load slightly faster in browsers.

.. _1283: https://httpolice.readthedocs.io/page/notices.html#1283
.. _1284: https://httpolice.readthedocs.io/page/notices.html#1284
.. _Prefer: https://tools.ietf.org/html/rfc7240
.. _1285: https://httpolice.readthedocs.io/page/notices.html#1285
.. _1291: https://httpolice.readthedocs.io/page/notices.html#1291
.. _1292: https://httpolice.readthedocs.io/page/notices.html#1292
.. _1293: https://httpolice.readthedocs.io/page/notices.html#1293
.. _1294: https://httpolice.readthedocs.io/page/notices.html#1294
.. _1295: https://httpolice.readthedocs.io/page/notices.html#1295
.. _analyzing TCP streams: https://httpolice.readthedocs.io/page/streams.html

Changed
-------
- Titles of many notices were changed to make more sense when viewed alone
  (as in text reports). If you depend on their wording (which you shouldn't),
  you may need to adjust.

Fixed
-----
- Notice `1021`_ is no longer reported on HTTP/2 requests.

.. _1021: https://httpolice.readthedocs.io/page/notices.html#1021

Meanwhile
---------
- `mitmproxy integration`_ has new features for interactive use.

.. _mitmproxy integration:
   https://mitmproxy-httpolice.readthedocs.io/


0.4.0 - 2017-01-14
~~~~~~~~~~~~~~~~~~

Added
-----
- Python 3.6 compatibility.
- Decompression of `brotli`_ compressed payloads (``Content-Encoding: br``).
- Checks for JSON charsets (notices `1280`_ and `1281`_).
- Checks for some wrong media types,
  currently ``plain/text`` and ``text/json`` (notice `1282`_).

.. _brotli: https://tools.ietf.org/html/rfc7932
.. _1280: https://httpolice.readthedocs.io/page/notices.html#1280
.. _1281: https://httpolice.readthedocs.io/page/notices.html#1281
.. _1282: https://httpolice.readthedocs.io/page/notices.html#1282

Removed
-------
- The deprecated constants
  ``httpolice.ERROR``, ``httpolice.COMMENT``, ``httpolice.DEBUG``
  have been removed. Use ``httpolice.Severity`` instead.
- When checking XML payloads, HTTPolice
  no longer takes precautions against denial-of-service attacks,
  because the `defusedxml`_ module does not currently work with Python 3.6.
  DoS attacks against HTTPolice are considered unlikely and non-critical.
- Notice 1275 ("XML with entity declarations") has been removed
  for the same reason.

.. _defusedxml: https://pypi.org/project/defusedxml/

Other
-----
- There is now a third-party `Chrome extension`_ for HTTPolice.

.. _Chrome extension: https://chrome.google.com/webstore/detail/httpolice-devtool/hnlnhebgfcfemjaphgbeokdnfpgbnhgn


0.3.0 - 2016-08-14
~~~~~~~~~~~~~~~~~~

Added
-----
- HTTPolice now caches more intermediate values in memory,
  which makes it significantly faster in many cases.
- HTTPolice now works correctly under `PyPy`_ (the 2.7 variant),
  which, too, can make it faster on large inputs.
  You will probably need a recent version of PyPy (5.3.1 is OK).
- `HTML reports`_ now have an "options" menu
  to filter exchanges and notices on the fly.
- The ``httpolice`` command-line tool now has
  a ``--fail-on`` option to exit with a non-zero status
  if any notices with a given severity have been reported.
- Work around various problems in HAR files exported by Firefox and `Fiddler`_.
- HTML reports can now display a remark before every request and response
  (enabled with the *Show remarks* checkbox in the "options" menu).
  The ``httpolice`` command-line tool puts the input filename in this remark.
  With the `Python API`_, you can put anything there
  using the ``remark`` argument to ``Request`` and ``Response`` constructors.
- Notices about HTTP/1.x framing errors (such as `1006`_)
  now include the input filename as well.
- Check for missing scheme name in authorization headers (notice `1274`_).
- Check for missing quality values in headers like Accept (notice `1276`_).
- Check for obsolete 'X-' prefix in experimental headers (notice `1277`_).
- Notice `1093`_ recognizes a few more product names as client libraries.

.. _HTML reports: https://httpolice.readthedocs.io/page/reports.html
.. _Fiddler: https://www.telerik.com/fiddler
.. _PyPy: http://pypy.org/
.. _Python API: https://httpolice.readthedocs.io/page/api.html
.. _1006: https://httpolice.readthedocs.io/page/notices.html#1006
.. _1093: https://httpolice.readthedocs.io/page/notices.html#1093
.. _1274: https://httpolice.readthedocs.io/page/notices.html#1274
.. _1276: https://httpolice.readthedocs.io/page/notices.html#1276
.. _1277: https://httpolice.readthedocs.io/page/notices.html#1277

Changed
-------
- For the `tcpick and tcpflow input`_ modes,
  you now have to use different options to tcpick/tcpflow (consult the manual).
- `Text reports`_ no longer show request/response numbers.
  If you parse these reports, you may need to adjust.
- Styles in HTML reports have been tweaked to make them more readable.

.. _Text reports: https://httpolice.readthedocs.io/page/reports.html

Deprecated
----------
- In the `Python API`_,
  the constants ``httpolice.ERROR``, ``httpolice.COMMENT``, ``httpolice.DEBUG``
  have been replaced with a single ``httpolice.Severity`` enumeration,
  and will be removed in the next release.

.. _Python API: https://httpolice.readthedocs.io/page/api.html

Fixed
-----
- The `tcpick and tcpflow input`_ modes should now be more reliable,
  although they still suffer from certain problems.
- CONNECT requests in HAR files are now handled correctly.
- Notices `1053`_ and `1066`_ are no longer reported
  on requests with bodies of length 0.

.. _tcpick and tcpflow input: https://httpolice.readthedocs.io/page/streams.html
.. _1053: https://httpolice.readthedocs.io/page/notices.html#1053
.. _1066: https://httpolice.readthedocs.io/page/notices.html#1066


0.2.0 - 2016-05-08
~~~~~~~~~~~~~~~~~~

Added
-----
- `Django integration`_ (as a separate distribution).
- Unwanted notices can now be `silenced`_.
- Checks for OAuth `bearer tokens`_.
- Checks for the `Content-Disposition`_ header.
- Checks for `RFC 5987`_ encoded values.
- Checks for `alternative services`_.
- Checks for HTTP/1.1 connection control features `prohibited in HTTP/2`_.
- `Stale controls`_ are now recognized.
- Checks for status code `451 (Unavailable For Legal Reasons)`_.

.. _Django integration: https://django-httpolice.readthedocs.io/
.. _silenced: https://httpolice.readthedocs.io/page/concepts.html#silence
.. _bearer tokens: https://tools.ietf.org/html/rfc6750
.. _Content-Disposition: https://tools.ietf.org/html/rfc6266
.. _RFC 5987: https://tools.ietf.org/html/rfc5987
.. _alternative services: https://tools.ietf.org/html/rfc7838
.. _prohibited in HTTP/2: https://tools.ietf.org/html/rfc7540#section-8.1.2.2
.. _Stale controls: https://tools.ietf.org/html/rfc5861
.. _451 (Unavailable For Legal Reasons): https://tools.ietf.org/html/rfc7725

Changed
-------
- `mitmproxy integration`_ has been moved into a separate distribution.

Fixed
-----
- Input files from tcpick are sorted correctly.
- Notice `1108`_ doesn't crash in non-English locales.
- Notices such as `1038`_ are not reported on responses to HEAD.

.. _1108: https://httpolice.readthedocs.io/page/notices.html#1108
.. _1038: https://httpolice.readthedocs.io/page/notices.html#1038


0.1.0 - 2016-04-25
~~~~~~~~~~~~~~~~~~

- Initial release.
