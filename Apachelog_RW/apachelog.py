import os
import re
import gzip
import bz2


def return_lines_from_file(fname):
    '''
    Generator - returns lines from any kind of files (plain, gzip, bzip)
    '''
    extension = os.path.splitext(fname)[-1]
    if extension == ".bz2":
        with bz2.BZ2File(fname, 'rb') as f:
            for line in f:
                yield line
    elif extension == ".gz":
        with gzip.open(fname, 'rb') as f:
            for line in f:
                yield line
    else:
        with open(fname, 'r') as f:
            for line in f:
                yield line


def lines_from_dir(filepat, dirname):
    '''
    Return sequence of lines from all files for the given `filepat`
    in directory `dirname`
    '''
    # !!!Your code here!!!
    path = r".\\"
    dirname = path + dirname
    tab_with_files =[]
    # print dirname
    for root, dirs, files in os.walk(dirname, topdown=True):
        files = [x for x in files if re.match(filepat, x)]
        for file in files:
            for line in return_lines_from_file(os.path.join(root, file)):
                yield line


def apache_log(lines):
    '''Parse log and map fields to dictionary key/value pairs'''
    list_with_dict = []
    pattern = re.compile("(.*?) (.*?) (.*?) \[(.*?)\] \"(.*?) (.*?) (.*?)\" (.*?) (.*)")
    for line in lines:
        match_obj = re.search(pattern, line)
        one_line_dict = {"status" : match_obj.group(8),
                         "proto" : match_obj.group(7),
                         "referrer" : match_obj.group(2),
                         "request" : match_obj.group(6),
                         "bytes" : match_obj.group(9),
                         "datetime" : match_obj.group(4),
                         "host" : match_obj.group(1),
                         "user" : match_obj.group(3),
                         "method" : match_obj.group(5) }
        yield one_line_dict
