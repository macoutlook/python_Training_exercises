import os
from distutils.core import setup, Command


class CheckTabs(Command):
    ''' TABs checker '''
     
    description = 'check if files contain TABs'
    user_options = []
     
    def initialize_options(self):
        'init options'
        pass

    def finalize_options(self):
        'finalize options'
        pass

    def run(self):
        'run command'
        for root, dirs, files in os.walk('.'):
            for name in files:
                fpath = os.path.join(root, name)
                if self._contains_tabs(fpath):
                    print 'ERROR: TABs in <%s>' % fpath

    def _contains_tabs(self, fpath):
        'Return True if `fpath` file contains tabs.'
        with open(fpath) as f:
            return '\t' in f.read()


setup(name='apachelog',
      version='1.0',
      author='<Your name>',
      py_modules=['apachelog', 'downloads', 'largest', 'status404'],
      cmdclass={'check_tabs': CheckTabs}
)
