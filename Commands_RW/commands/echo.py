from comm import Command


class Echo(Command):
    cmd_name = 'echo'
    cmd_description = 'Echo "Hello, World!!!"'

    def execute(self):
        self._run(['echo', 'Hello, World!!!'])

