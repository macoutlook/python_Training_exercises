import ConfigParser
import os
import logging


class ConfParser(object):

    def __init__(self, file_path, log_level = logging.DEBUG):
        self.__Config = ConfigParser.ConfigParser()
        if os.path.isfile(file_path):
            self.__logger = logging.getLogger(self.__class__.__name__)
            self.__logger.setLevel(log_level)
            self.__Config.read(file_path)
            if self.__get_sections():
                self.__parse_all()
        else:
            self.__logger.warning("Configuration .ini file does not exists")

    def __get_sections(self):
        sections = self.__Config.sections()
        result = False

        if sections[0] == "TelnetConfig":
            self.__telnet_section = "TelnetConfig"
            result = True
        else:
            self.__logger.warning(".ini file is not proper")

        return result

    def __parse_all(self):
        self.telnet_conf_dict = self.__parse_section(self.__telnet_section)

    def __parse_section(self, section):
        # By Config.options we can get all options for section, by Config.get we can get value for section and option
        options = self.__Config.options(section)
        dict_with_values = {}

        for option in options:
            dict_with_values[option] = self.__Config.get(section, option)
        self.__logger.debug(".ini file was successfully read")

        return dict_with_values
