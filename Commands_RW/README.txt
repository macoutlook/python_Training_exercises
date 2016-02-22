
TASK
----------

Create application, which will execute user defined commands provided as modules
in subdirectory `commands`.
So having such files:

.
|-- commands
|   |-- echo.py
|   `-- ls.py
|-- commands.py
`-- main.py

example session should look like this:

# main program executed without parameters should display help message,
# which contain all available commands with descriptions

$ python main.py
Usage: main.py [-h | --help] [-v | --verbose] <echo | ls>
    echo           - Echo "Hello, World!!!"
    ls             - list current directory


# executed with command name and "-v" switch should display log messages
# to standard output

$ python main.py -v echo
DEBUG root - START
INFO Echo - Command: echo Hello, World!!!
DEBUG Echo - output: 'Hello, World!!!\n'
DEBUG root - DONE

# executed with command name, that does not exist, should display error message

$ python main.py -v xx
DEBUG root - START
ERROR root - Command error: Command <xx> not implemented
DEBUG root - DONE


The whole idea boils down to the fact that in `commands` module there is implemented
class `Command` and modules in subdirectory `commands` contain classes,
which inherit from `Command` class. Using special method `__subclasses__` of `Command`
class there can be found all loaded subclasses, thus user defined commands.

`Command` class has two class atributes: cmd_name, cmd_description, which should be
used for displaying imformation about available commands and for finding command
to be executed.

You should complete code provided in files `main.py`, `commands.py` 
(sections: !!!Your code here!!!).
On the basis of `commands/echo.py` implementation, there should be added 
another command `commands/ls.py`, which should list content of the current directory.
For this puprose should be executed external command `ls` in Linux or `dir` in Windows.
There is already implemented `_run` method, which can be used for it.
So the output from the command should look as follows:

# without "-v" no ouptut at all
$ python main.py ls

# with "-v" debug information
$ python main.py -v ls
DEBUG root - START
INFO Echo - Command: dir
DEBUG Echo - output: 'commands  commands.py  commands.pyc  main.py\n'
DEBUG root - DONE



TIPS
--------------
1. For handling program input options/parameters use `getopt` module
2. Output messages should be generated with help of `logging` module 
   in the format "%(levelname)s %(name)s - %(message)s".
   Logging configuration should be added to `_configlog` function.
3. All modules from `commands` directory should dynamically imported
   and that part has been already implemented in `load_commands` function


