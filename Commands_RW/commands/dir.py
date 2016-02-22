from comm import Command


class Dir(Command):
    cmd_name = 'dir'
    cmd_description = 'list current directory"'

    def execute(self):
        self._run(['Dir', '/b'])