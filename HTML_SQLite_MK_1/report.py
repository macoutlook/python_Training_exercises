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

    def prepare_generating(self, logg_hndl):
        class_name = self.__class__.__name__

        if self.generate_report():
            logg_hndl.prepare_other_notification("%s Report was successfully generated" % class_name )
        else:
            logg_hndl.prepare_other_notification("%s Report was not generated successfully" % class_name, logging.ERROR)
