from cmd import Cmd
from My_Style import (
    Color,Style,Animation,is_exist
    )
import os ,sys ,json ,time
Color.Theme('light')
XPATH = os.getcwd()

HELP ='''
 sections:
-------------------------------------------
  show       To display the tools.
  options    Display the options menu.
  download   To download the tools.
  main       main page.
-------------------------------------------
'''
OPTIONS = '''
 options:
-------------------------------------------
  path : {}
-------------------------------------------
'''

# all tools clone...
with open(XPATH+'/tools/Tools/clone.json') as file:CLONES = json.load(file)

def intro_text(type=True):
    S = 'G#[Y#+G#]'
    if type:
        return Style(HELP).Square(
        Square=[S,' G#| ',S,'-',S,' G#|',S,'-'])
    else:
        Animation.SlowLine( Style(HELP).Square(
        Square=[S,' G#| ',S,'-',S,' G#|',S,'-']
        ),t=0.03)

class Tools_shell(Cmd):
    prompt = Color.reader(f'G#┌───B#[ C#{os.uname().sysname}B# ]G##B#[ Y#{os.uname().nodename} B#]G##B#[ R#Tools B#]G#>>>\nG#|\nG#└─>>>$ W#')
    intro = intro_text()
    path = os.environ['HOME']
    shell_main = None

    def __init__(self):
        super().__init__()
        self.tools_name = []
        for key,clone in CLONES.items():
            self.tools_name.append(key)
        self.tools_name.sort()

    def help(self):
        return intro_text()

    def default(self, line):
        sys.stdout.write('bash: %s: command not found\n'%line)

    def do_help(self,arg):
        if arg:
            super().do_help(arg)
        else:
            intro_text(type=False)

    def do_clear(self,arg):
        os.system('clear')

    def do_exit(self,arg):
        exit()

    def do_main(self,arg):
        self.shell_main()

    def do_options(self,arg):
        S = 'G#[Y#+G#]'
        print(Style(OPTIONS.format(self.path)).Square(
        Square=[S,' G#| ',S,'-',S,' G#|',S,'-']))

    def do_set(self,arg):
        PATH = arg.replace('path','').strip()
        CHECK = os.path.isdir(PATH)
        if 'path' in arg and CHECK:
            self.path = PATH
            print(Color.reader(f'G# Done :{PATH}'))
        else :
            print(f'path: {PATH}: not exist')

    def complete_set(self, text, line, begidx, endidx):
        LIST = ['path']
        if 'path' in line:
            return None
        return LIST

    def do_show(self,arg):
        tools_name = self.tools_name
        for name in tools_name:
            print(Color.reader(f'B#> W#{name}'))
            time.sleep(0.01)
        print (Color.reader(f'B#There are R#{len(tools_name)}B# toolsY#.P#.G#.\n'))

    def do_download(self,arg):
        tools_to_download = arg.split(' ')
        my_path = os.getcwd()
        for i in tools_to_download:
            if is_exist('sudo'):
                git = 'sudo git clone '
            else:
                git = 'git clone '
            os.chdir(self.path)
            os.system(git+CLONES[i])
            print('\n')
        os.chdir(my_path)

    def complete_download(self, text, line, begidx, endidx):
        if not text:
            completions = self.tools_name[:]
        else:
            completions = [
                f
                for f in self.tools_name
                if f.startswith(text)
            ]
        return completions
