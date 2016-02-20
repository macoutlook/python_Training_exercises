import argparse
import logging_handler
from sqlite_report import SqlLiteReport
from html_report import HtmlReport
import utilities

logg_hndl = None


def argument_parse():
    # argparse module is used for parsing arguments
    # can use option like action='name_of_method' and dest='var_name'
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Give path to log file")
    parser.add_argument("reg_exp", type=str, help="Information if program should use regular expressions, type True or False")
    parser.add_argument("path_to_result", type=str, help="Path to file where result should be written")
    parser.add_argument("rep_type", type=str, help="Type of report, True means report will be in html, False means report will be in sqlite")
    parser.add_argument("searched_phrase", type=str, help="Phrase which should be found")

    return parser.parse_args()


def main():
    '''Main function'''
    global logg_hndl
    logg_hndl = logging_handler.LoggingHandler()
    args = argument_parse()
    rep_obj = None
    # There is problem with get bool type from arguments, and there is convertion from int to bool
    is_re = utilities.str_to_bool(args.reg_exp)
    list_with_found = utilities.search_in_file(args.path, is_re, args.searched_phrase, logg_hndl)
    # Report can be created to .html or .db file, accordingly flag in parameters
    if args.rep_type == "html":
            rep_obj = HtmlReport(list_with_found, args.path_to_result, args.searched_phrase)
    elif args.rep_type == "sqlite":
            rep_obj = SqlLiteReport(list_with_found, args.path_to_result)

    if rep_obj:
        rep_obj.prepare_generating(logg_hndl)

    logg_hndl.end_logging()

if __name__ == '__main__':
    main()
