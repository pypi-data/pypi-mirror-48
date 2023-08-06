# GetCCWarc
#######
|PyPI-Status| |PyPI-Versions| |Build-Status| |LICENCE|

Easily get a web-page from stored commmoncrawl WARC files on S3

Usage:

.. code-block:: python

  >>> from GetCCWarc import GetCCWarc
  >>> off, len, file = 437157916, 884, "crawl-data/CC-MAIN-2019-22/segments/1558232256040.41/warc/CC-MAIN-20190520142005-20190520164005-00160.warc.gz"
  >>> warc = GetCCWarc.get_warc_file(file, len, off, gzip=False)
  >>> print(warc)



.. |PyPI-Status| image:: https://img.shields.io/pypi/v/GetCCWarc.svg
  :target: https://pypi.python.org/pypi/GetCCWarc

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/GetCCWarc.svg
   :target: https://pypi.python.org/pypi/GetCCWarc

.. |Build-Status| image:: https://travis-ci.org/ohadzad/GetCCWarc.svg?branch=master
  :target: https://travis-ci.org/ohadzad/GetCCWarc

.. |LICENCE| image:: https://img.shields.io/pypi/l/GetCCWarc.svg
  :target: https://pypi.python.org/pypi/GetCCWarc
