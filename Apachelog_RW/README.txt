
TASK
--------------

In this exercise there should be parsed all apache log files located under directory `www`.
There are uncompressed, gzip-ed and bzip-ed log files. All of them should be processed.

Every line in those logs has following structure:

<host> <referrer> <user> [<datetime>] "<method> <request> <proto>" <status> <bytes>

This line should be parsed using regular expression and result written to the dictionary like this:

{'status' : '200',
'proto' : 'HTTP/1.1',
'referrer': '-',
'request' : '/ply/ply.html',
'bytes' : '97238',
'datetime': '24/Feb/2008:00:08:59 -0600',
'host' : '140.180.132.213',
'user' : '-',
'method' : 'GET'}

So basically parsing all logs should give sequence of such dictionaries.
All parsing stuff should be implemented in the file `apachelog.py`.
In this file there have been already created two functions: `lines_from_dir` and `apache_log`,
which will be used by other programs (read below).
Basically `lines_from_dir` should return sequence of lines from all log files
and `apache_log` should transform sequence of lines into sequence of dictionaries.

Additionaly there should be created small programs, which will use
`apachelog` module for executing simple queries on log files.

There should be prepared following programs:

1. downloads.py

Display number of downloads of file "/ply/ply-2.3.tar.gz".
From every line of all apache logs should be extracted field <request>
and compared with "/ply/ply-2.3.tar.gz" string and number of such records
displayed to standard output.

Example output:

$ python downloads.py
Total: 690

In `downloads.py` file there should be completed implementation of `get_downloads_count` function.
Additionaly there should be added doctests [1]_ for this function.


2. largest.py

Display the largest data transfer found in logs.
From every line of all apache logs should be extracted fields <bytes> and <request>.
For maximum <bytes> value should be displayed record:
<bytes> <request>

Example ouptut:

$ python largest.py
4919642 /dynamic/ffcache.zip

In `largest.py` file there should be completed implementation of `get_largest` function.
Additionaly there should be added doctests [1]_ for this function.

3. status404.py

Display set of all unique requests with status equal to "404".
From every line of all apache logs should be extracted fields <status> and <request>.
For each field <status> equal to "404" there should be displayed unique record:
<request>

Example output:

$ python status404.py
/02WorkingWithData.pdf
/06FilesAndText.pdf

In `status404.py` file there should be completed implementation of `get_404` function.
Additionaly there should be added doctests [1]_ for this function.


TIPS
---------

1. Try to use generators [2]_ as much you can
2. Consider using `os.walk` function for traversing directory with log files
3. Consider implementing general function, which will return generator/sequence of all
   open file objects. This function should take care of the file type: plain, gzip, bzip


.. [1] http://docs.python.org/2/library/doctest.html
.. [2] http://docs.python.org/2/tutorial/classes.html#generators
