import os
import re


def lines_from_dir(filepat, dirname):
    '''
    Return sequence of lines from all files for the given `filepat`
    in directory `dirname`
    '''
    # !!!Your code here!!!
    #http://docs.python.org/2/tutorial/classes.html#generators
    path = r".\\"
    dirname = path + dirname
    tab_with_files =[]
    # print dirname
    for root, dirs, files in os.walk(dirname, topdown=True):
        for name in files:
            if name == filepat:
                # print(os.path.join(root, name))
                tab_with_files.append(os.path.join(root, name))
    #print tab_with_files
    file_object = open(tab_with_files[0])
    lines = file_object.readlines()
    #print lines[2]
    list_with_dict = apache_log(lines)
    return list_with_dict


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
        list_with_dict.append(one_line_dict)
    return list_with_dict


def read_in_chunks(file_object):
    while file_object:
        data = file_object.Readline()
        if not data:
            break
        yield data