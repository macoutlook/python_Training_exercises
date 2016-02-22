import logging
import sys


class LoggingHandler(object):
    log_level = logging.DEBUG

    def __init__(self, file_path, log_lvl = log_level):
        self.logger = logging.getLogger()
        logging.basicConfig(filename=file_path, level=log_lvl)
        self.logger.info("Program starts")

    def initiate_stdout_logging(self):
        ch = logging.StreamHandler(sys.stdout)
        self.logger.addHandler(ch)

    def prepare_other_notification(self, msg, level=log_level):
        if level == logging.DEBUG:
            self.logger.debug(msg)
        elif level == logging.INFO:
            self.logger.info(msg)
        elif level == logging.WARNING:
            self.logger.warning(msg)
        elif level == logging.ERROR:
            self.logger.error(msg)

    def end_logging(self):
        self.logger.info("End of program")
