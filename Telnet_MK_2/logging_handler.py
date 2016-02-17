import logging


class LoggingHandler(object):
    log_level = logging.DEBUG

    def __init__(self, file_path, log_lvl = log_level):
        logging.basicConfig(filename=file_path, level=log_lvl)
        logging.info("Program starts")

    @staticmethod
    def prepare_other_notification(msg, level=log_level):
        if level == logging.DEBUG:
            logging.debug(msg)
        elif level == logging.INFO:
            logging.info(msg)
        elif level == logging.WARNING:
            logging.warning(msg)
        elif level == logging.ERROR:
            logging.error(msg)

    @staticmethod
    def end_logging():
        logging.info("End of program")
