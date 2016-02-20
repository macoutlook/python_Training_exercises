import logging
import re


def str_to_bool(conv_str):
    return conv_str.lower() in ("true")


def search_in_file(path, is_regexp, searched_phrase, logg_hndl):
    """
    this method is used for getting all lines from log file and returns list of lines
    :param path: this is a path for log file
    :param is_regexp: flag which indicate that parsing should be with regular expressions
    :param searched_phrase: this is phrase which should be searched
    :return: list with lines
    """
    file = open(path)
    lines = file.readlines()
    list_with_dicts = []
    if(is_regexp):
        list_with_dicts = find_with_re(lines, searched_phrase, logg_hndl)
    else:
        list_with_dicts = find_without_re(lines, searched_phrase, logg_hndl)
    file.close()

    return list_with_dicts


def find_with_re(lines, searched_phrase, logg_hndl):
    """
    this method is used for parsing log file with regular expressions
    :param lines: list of lines
    :param searched_phrase:
    :return: as a result it gives list with lines, where searched_phrase was found
    """
    logg_hndl
    list_with_dicts = []
    # regex = ".*" + searched_phrase + "(([\d,-]+[^,]*$)|([\d,-]+.*?), ) "
    # .* CHANGE : (([\d,-]+[^,]*$)|([\d,-].*?),)
    regex = ".*" + searched_phrase + "(((.*?), )|(.*$))"

    for line in lines:
        matchObj = re.match(regex, line)
        if matchObj:
            if matchObj.group(3) == None:
                value = matchObj.group(1)
            else:
                value = matchObj.group(3)
            if(value != None):
                matched_date_time = re.match("\[(.*?) (.*?)\] .*", line)
                date = matched_date_time.group(1)
                time = matched_date_time.group(2)
                one_dict = {searched_phrase[:-2]: value, "date": date, "time": time}
                list_with_dicts.append((one_dict))
    list_len = list_with_dicts.__len__()

    if list_len > 0:
        logg_hndl.prepare_other_notification("Given phrase was successfully found with regular expressions in given log file %s times" % list_len)
    else:
        logg_hndl.prepare_other_notification("Unfortunately given phrase was not found in given log file", logging.WARNING)

    return list_with_dicts


def find_without_re(lines, searched_phrase, log_hndl):
    """
    This method uses str module to parsing, spliting and finding searched_phrase
    :param lines:
    :param searched_phrase:
    :return: list with lines with searched_phrase
    """
    list_with_dicts = []

    for line in lines:
        result = line.split(", ")
        for word in result:
            # finding word in string
            found_ind = word.find(searched_phrase)
            if found_ind != -1:
                found_ind += len(searched_phrase)
                value = (word[found_ind:])
                date_time = result[0]
                date_time = date_time.split(" ")
                date = date_time[0]
                date = date[1:]
                time = date_time[1]
                # time is got without last character
                time = time[:-1]
                one_dict = {searched_phrase[:-2]: value, "date": date, "time": time}
                list_with_dicts.append((one_dict))
    list_len = list_with_dicts.__len__()

    if list_len > 0:
        log_hndl.prepare_other_notification("Given phrase was successfully found in given log file %s times" % list_len)
    else:
        log_hndl.prepare_other_notification("Unfortunately given phrase was not found in given log file", logging.WARNING)

    return list_with_dicts