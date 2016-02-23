from comm import Command
from sys import platform as _platform


class Ls(Command):
    cmd_name = 'ls'
    cmd_description = 'list current directory"'

    def execute(self):
        if _platform == "win32" or _platform == "win64":
            self._run(['dir', '/b'])
        elif _platform == "linux" or _platform =="linux2":
            self._run(['ls', '-l'])
