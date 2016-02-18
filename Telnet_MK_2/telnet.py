import telnetlib
import socket
import logging


class Telnet(object):
    glob_prompt = ':~$'
    glob_timeout = 25

    def __init__(self, host = "localhost", user_name = "root", password = "root", port = 23, log_level = logging.DEBUG):
        self.__telnet_conn = None
        self.host = host
        self.port = port
        self.__username = user_name
        self.__password = password
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__logger.setLevel(log_level)

        try:
            self.__telnet_conn=telnetlib.Telnet(self.host)
            self.__logger.debug("Telnet connection is open")
        except socket.error as e:
            self.__logger.error(e)

    def init_connection(self, prompt=glob_prompt, timeout=glob_timeout):
        if self.__telnet_conn:
            try:
                self.__logger.debug(self.__telnet_conn.read_until("login:"))
                self.__telnet_conn.write(self.__username + "\n")
                self.__logger.debug(self.__telnet_conn.read_until("Password: "))
                self.__telnet_conn.write(self.__password + "\n")
                self.__logger.debug(self.__telnet_conn.read_until(prompt, timeout=timeout))
            except (EOFError, socket.error) as e:
                self.__logger.error(e)
        else:
            self.__logger.error("Unfortunately Telnet connection was not created")

    def execute_commands(self, list_with_commands, prompt=glob_prompt, timeout=glob_timeout):
        all_command = ''

        if self.__telnet_conn:
            for command in list_with_commands:
                for el in command:
                    all_command += el
                try:
                    self.__logger.debug("Execute command %s" % all_command)
                    self.__telnet_conn.write(all_command + "\n")
                    self.__logger.debug(self.__telnet_conn.read_until(prompt, timeout=timeout))
                except (EOFError, socket.error) as e:
                    self.__logger.error(e)
                    break
                all_command = ''

    def close_connection(self):
        if self.__telnet_conn:
            self.__telnet_conn.close()
            self.__logger.debug("Telnet connection is closed")
