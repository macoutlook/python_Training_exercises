from abc import ABCMeta, abstractmethod
import logging


class Report(object):
    __metaclass__ = ABCMeta

    def __init__(self, list_with_records, file_path, log_level = logging.DEBUG):
        self.list_with_records = list_with_records
        self.file_path = file_path

    @abstractmethod
    def generate_report(self):
        return "Generating report should be implemented here"
