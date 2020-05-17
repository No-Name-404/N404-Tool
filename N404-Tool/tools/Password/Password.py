from N4Tools.Design import (
    Color,Style,Animation
    )
from tools.root import (
HELP_PASSWORD as HELP,
OPTIONS_PASSWORD as OPTIONS,
SHELL_ALL)

# >>> x = ('3*'*3)[0:-1]
# >>> exec(f'print({x})')

class Password_shell(SHELL_ALL):
    # the shell command...
    page = 'Password'

    def __init__(self):
        super().__init__()

    def help(self):
        return self.SQUARE(HELP)

    def do_options(self,arg):
        print (self.SQUARE(OPTIONS))
