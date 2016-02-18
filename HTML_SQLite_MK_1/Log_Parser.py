import argparse
import re
import html_report
import sqlite_report
import logging_handler
import logging

logg_hndl = None


def search_in_file(path, is_regexp, searched_phrase):
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
        list_with_dicts = find_with_re(lines, searched_phrase)
    else:
        list_with_dicts = find_without_re(lines, searched_phrase)
    file.close()

    return list_with_dicts


def find_with_re(lines, searched_phrase):
    """
    this method is used for parsing log file with regular expressions
    :param lines: list of lines
    :param searched_phrase:
    :return: as a result it gives list with lines, where searched_phrase was found
    """
    global logg_hndl
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


def find_without_re(lines, searched_phrase):
    """
    This method uses str module to parsing, spliting and finding searched_phrase
    :param lines:
    :param searched_phrase:
    :return: list with lines with searched_phrase
    """
    global logg_hndl
    list_with_dicts = []

    for line in lines:
        result = line.split(", ")
        for word in result:
            #finding word in string
            found_ind = word.find(searched_phrase)
            if found_ind != -1:
                found_ind += len(searched_phrase)
                value = (word[found_ind:])
                date_time = result[0]
                date_time = date_time.split(" ")
                date = date_time[0]
                date = date[1:]
                time = date_time[1]
                #time is get without last character
                time = time[:-1]
                one_dict = {searched_phrase[:-2]: value, "date": date, "time": time}
                list_with_dicts.append((one_dict))
    list_len = list_with_dicts.__len__()

    if list_len > 0:
        logg_hndl.prepare_other_notification("Given phrase was successfully found in given log file %s times" % list_len)
    else:
        logg_hndl.prepare_other_notification("Unfortunately given phrase was not found in given log file", logging.WARNING)

    return list_with_dicts


def argument_parse():
    #argparse module is used for parsing arguments
    #can use option like action='name_of_method' and dest='var_name'
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Give path to log file")
    parser.add_argument("reg_exp", type=str, help="Information if program should use regular expressions, type True or False")
    parser.add_argument("path_to_result", type=str, help="Path to file where result should be written")
    parser.add_argument("is_rep_html", type=str, help="Type of report, True means report will be in html, False means report will be in sqlite")
    parser.add_argument("searched_phrase", type=str, help="Phrase which should be found")

    return parser.parse_args()


def main():
    '''Main function'''
    global logg_hndl
    logg_hndl = logging_handler.LoggingHandler()
    args = argument_parse()
    #There is problem with get bool type from arguments, and there is convertion from int to bool
    if(args.reg_exp == "True"):
        args.reg_exp = True
    elif(args.reg_exp == "False"):
        args.reg_exp = False
    #There is problem with get bool type from arguments, and there is convertion from int to bool
    if(args.is_rep_html == "True"):
        args.is_rep_html = True
    elif(args.is_rep_html == "False"):
        args.is_rep_html = False

    list = search_in_file(args.path, args.reg_exp, args.searched_phrase)
    #Report can be created to .html or .db file, accordingly flag in parameters
    if args.is_rep_html == True:
        html_rep = html_report.HtmlReport(list, args.path_to_result, args.searched_phrase)
        if html_rep.generate_report():
            logg_hndl.prepare_other_notification("HTML Report was successfully generated")
        else:
            logg_hndl.prepare_other_notification("HTML Report was not generated successfully", logging.ERROR)
    else:
        sqlite_rep = sqlite_report.SqlLiteReport(list, args.path_to_result)
        if sqlite_rep.generate_report():
            logg_hndl.prepare_other_notification("Sqlite Report was successfully generated")
        else:
            logg_hndl.prepare_other_notification("Sqlite Report was not generated successfully", logging.ERROR)

    logg_hndl.end_logging()

if __name__ == '__main__':
    main()
