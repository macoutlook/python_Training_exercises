import os
from os.path import join, normpath, dirname, basename, splitext
import sys
import getopt
import logging
import fnmatch

import comm


def load_commands():
    '''
    Load commands from external modules
    located in subdirectory `commands`
    '''
    path = normpath(join(dirname(__file__), 'commands'))
    cmdlst = os.listdir(path)
    cmdlst = fnmatch.filter(cmdlst, '*.py')
    cmdlst = map(lambda p: splitext(p)[0], cmdlst)
    if not path in sys.path:
        sys.path.insert(0, path)
    for cmd in cmdlst:
        mod = __import__(cmd, globals(), locals(), [])
        if not mod:
            raise RuntimeError('Module <%s> import failed!' % cmd)


def _configlog(loglevel):
    '''
    Configure logging
    '''
    # !!!Your code here!!!
    FORMAT = '%(levelname)s %(name)s - %(message)s'
    logging.basicConfig(format=FORMAT)
    logger = logging.getLogger()
    logger.setLevel(loglevel)

    return logger


def _usage(prog):
    '''
    Display program help message to standard output
    '''
    s = 'Usage: %s [-h | --help] [-v | --verbose]'
    # add information about available commands in subdirectory `commands`
    # in the form:
    #     <command name>           - <command description>
    # !!!Your code here!!!
    print s % basename(prog)

    for one_comm in comm.get_commands_all():
        print "%s      - %s" % (one_comm.cmd_name, one_comm.cmd_description)
    sys.exit(1)


def main(argv):
    loglevel = logging.ERROR
    load_commands()

    # handle input switches and parameters using `getopt.getopt` function
    # there should be handled following switches:
    # -h and --help   - display help message prepared in _usage function above
    # -v and --verbose  - display additional debug ouput, set log level as logging.DEBUG
    #
    # There should be accepted only one input parameter, namely <command name>
    #
    # Missing input parameters should cause displaying help message.
    # Wrong command name in the first parameter, should cause displaying error message.
    try:
        options, args = getopt.getopt(sys.argv[1:], 'hv', ['help','verbose'])

        if not options and not args:
            _usage(os.path.realpath(__file__))
        for opt in options:
            if '-h' in opt or '--help' in opt:
                _usage(os.path.realpath(__file__))
            elif '-v' in opt or '--verbose' in opt:
                loglevel = logging.DEBUG

        command = args[0]
        logger = _configlog(loglevel)
        logger.debug('START')
        try:
            cmdclass = comm.get_command(command)

            # execute command provided by user as first parameter
            # `cmdclass` it should be class, which implements given command
            # this class should be instantiated with appropriate arguments
            # and `execute` method of this instance should be called
            #
            cmd_object = cmdclass(loglevel=loglevel)
            cmd_object.execute()

        except Exception, ex:
            logger.error('Command error: %s' % ex)
        logger.debug('DONE')
    except getopt.GetoptError as e:
        print e


if __name__ == '__main__':
    main(sys.argv)
