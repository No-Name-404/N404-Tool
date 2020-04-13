import os
from My_Style import Color,Style,Animation
from cmd import Cmd
Color.Theme('light')

# DESIGN and CODE - ALL TOOL...
PROMPT = lambda text:Color.reader(f'G#┌───B#[ C#{os.uname().sysname}B# ]G##B#[ Y#{os.uname().nodename} B#]G##B#[ R#{text} B#]G#>>>\nG#|\nG#└─>>>W#$ \033[0;37m')

class SHELL_ALL(Cmd):
    shell_main = None
    path = os.environ['HOME'] # user path (home or root)
    tool_path = os.getcwd()

    def __init__(self):
        super(SHELL_ALL,self).__init__()
        self.intro = self.help()

    def SQUARE(self,HELP,type=True):
        S = 'G#[Y#+G#]'
        if type:
            return Style(HELP).Square(
            Square=[S,' G#| ',S,'-',S,' G#|',S,'-'])
        else:
            Animation.SlowLine(HELP,t=0.02)

    def default(self, line):
        '''
        if user enter a wrong command,
        this message will be display
        '''
        print('bash: %s: command not found'%line)

    def do_clear(self,arg):
        os.system('clear')

    def do_exit(self,arg):
        exit()

    def do_help(self,arg):
        if arg: # check if run as intro
            super().do_help(arg) # display help text
        else:
            self.SQUARE(self.help(),type=False) # display help text as Animation

    def help(self):
        return 'text'

    def do_main(self,arg):
        try:
            self.shell_main()
        except TypeError:
            print ('This is the Main page...')
