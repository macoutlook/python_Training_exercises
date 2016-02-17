import ConfigParser


class ConfParser(object):

    def __init__(self, path):
        self.__Config = ConfigParser.ConfigParser()
        self.__Config.read(path)
        if self.__get_sections():
            self.__parse_all()
        else:
            print "Problem with parsing configuration file"

    def __get_sections(self):
        result = False
        sections = self.__Config.sections()

        if sections[0] == SectionType.WebDriverConf:
            self.__web_driver_conf = SectionType.WebDriverConf
        else:
           print "Problem with WebDriverConf section in .ini file"
        if sections[1] == SectionType.xpaths:
            self.__xpath= SectionType.xpaths
            result = True
        else:
            print "Problem with xpaths section in .ini file"
            result = False
        return result

    def __parse_all(self):
        self.web_driver_conf_dict = self.__parse_section(self.__web_driver_conf)
        self.xpath_list = self.__parse_section(self.__xpath)

    def __parse_section(self, section):
        # By Config.options we can get all options for section, by Config.get we can get value for section and option
        options = self.__Config.options(section)
        dict_with_values = {}
        list_with_values = []

        for option in options:
            dict_with_values[option] = self.__Config.get(section, option)
            list_with_values.append(self.__Config.get(section, option))

        if section == SectionType.WebDriverConf:
            return dict_with_values
        elif section == SectionType.xpaths:
            return list_with_values


class SectionType():
    WebDriverConf = "WebDriverConf"
    xpaths = "xpaths"


