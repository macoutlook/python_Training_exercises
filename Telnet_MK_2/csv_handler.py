import csv
import os
import logging


class CsvHandler(object):

    def __init__(self, file_path, log_level = logging.DEBUG):
        self.__file_path = file_path
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__logger.setLevel(log_level)
        self.__logger.debug(".csv file is read")

    def read_csv(self):
        list_with_comm = []

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'rb') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
                for row in csv_reader:
                    list_with_comm.append(row)
            self.__logger.debug(".csv file was successfully read")
        else:
            self.__logger.warning(".csv file doesn't exists")

        return list_with_comm
