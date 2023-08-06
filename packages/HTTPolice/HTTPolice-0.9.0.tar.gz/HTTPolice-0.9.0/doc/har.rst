Analyzing HAR files
===================

.. highlight:: console

`HAR`__ is a quasi-standardized JSON format for saving HTTP traffic.
It is supported by many HTTP-related tools,
including developer consoles of some Web browsers.

__ https://en.wikipedia.org/wiki/.har

HTTPolice can analyze HAR files with the ``-i har`` option::

  $ httpolice -i har myfile.har

However, please note that HAR support in exporters is **erratic**.
HTTPolice tries to do a reasonable job on files exported from
major Web browsers and some other HTTP tools, but some information is lost
and some checks are skipped to avoid false positives.

If HTTPolice gives unexpected results on your HAR files,
feel free to `submit an issue`__ (don’t forget to attach the files),
and I’ll see what can be done about it.

__ https://github.com/vfaronov/httpolice/issues
