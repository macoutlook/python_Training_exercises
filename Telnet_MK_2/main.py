import argparse
import configparser
import telnet
import csv_handler
from logging_handler import LoggingHandler
import logging


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_ini", type=str, help="Give path to .ini file")
    parser.add_argument("path_to_csv", type=str, help="Give path to .csv file with telnet commands")
    parser.add_argument("path_to_log", type=str, help="Give path to log file")
    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    ini_file_path = args.path_to_ini
    csv_file_path = args.path_to_csv
    log_file_path = args.path_to_log

    logg_hndl = LoggingHandler(log_file_path)

    csv_reader = csv_handler.CsvHandler(csv_file_path)
    list_with_comm = csv_reader.read_csv()

    conf_parser = configparser.ConfParser(ini_file_path)

    try:
        telnet_client = telnet.Telnet(conf_parser.telnet_conf_dict["ip"], conf_parser.telnet_conf_dict["user_name"], conf_parser.telnet_conf_dict["password"])
    except KeyError as e:
        msg = "Problem with wrong key: %s in .ini file" % e
        logg_hndl.prepare_other_notification(msg, logging.ERROR)
        telnet_client = telnet.Telnet()

    telnet_client.init_connection()
    telnet_client.execute_commands(list_with_comm)
    telnet_client.close_connection()

    LoggingHandler.end_logging()
    print "Program terminates, log is available in path: %s" % log_file_path

if __name__ == '__main__':
    main()
