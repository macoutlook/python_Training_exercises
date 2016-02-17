import os
import confparser
import webdriver
import argparse
import urlparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_ini", type=str, help="Give path .ini file")
    args = parser.parse_args()
    file_path = args.path_to_ini
    confparser_obj = confparser.ConfParser(file_path)
    try:
        webdriv_obj = webdriver.WebDriverHandler(confparser_obj.web_driver_conf_dict['chromedriverpath'], confparser_obj.web_driver_conf_dict['url'], confparser_obj.xpath_list, file_path)
        webdriv_obj.execute_invokes()
    except KeyError as e:
        print "Unfortunately there were problems", e


if __name__ == '__main__':
    main()