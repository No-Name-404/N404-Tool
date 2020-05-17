from N4Tools.Design import (
    Color,Style,Animation
    )

from N4Tools.System import is_in_bin
import os ,sys ,json ,time ,subprocess
Color.Theme('light')

from tools.root import (
HELP_TOOLS as HELP,
OPTIONS_TOOLS as OPTIONS,
SHELL_ALL,
TOOLS_PATH,
XPATH )

# all tools clone...
with open(TOOLS_PATH+'Tools/.clone.json') as file:
    CLONES = json.load(file)

class Tools_shell(SHELL_ALL):
    # the shell command...
    page = 'Tools'

    def __init__(self):
        super(Tools_shell,self).__init__()
        # Sort the list of tools by alphabet...
        self.tools_name = []
        for key,clone in CLONES.items():
            self.tools_name.append(key)
        self.tools_name.sort()

    def help(self):
        return  self.SQUARE(HELP)

    def do_options(self,arg):
        print( self.SQUARE(OPTIONS.format(self.path)) )

    def do_set(self,arg):
        PATH = arg.replace('path','').strip()
        CHECK = os.path.isdir(PATH)
        if 'path' in arg and CHECK:
            self.path = PATH
            print(Color.reader(f'G#Y#path C#: W#{PATH}'))
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
        print (Color.reader(f'B#There are R#{len(tools_name)}B# toolsW#...\n'))

    def do_download(self,arg):
        tools_to_download = arg.split(' ')
        print ('please wait...')
        for i in tools_to_download:
            if is_in_bin('sudo'):
                git = 'sudo git clone '
            else:
                git = 'git clone '
            os.chdir(self.path)
            try:
                tool = subprocess.run(git+CLONES[i],shell=True,capture_output=True)
                if 'already exists and' in tool.stderr.decode('utf-8'):
                    print(Color.reader(f'\033[0;37m[ Y#OK \033[0;37m] {i} has been downloaded...'))
                elif len(tool.stderr.decode('utf-8').split(' ')) == 3:
                    print(Color.reader(f'\033[0;37m[ G#OK \033[0;37m] {i} has been downloaded...'))
                else:
                    print(Color.reader(f'\033[0;37m[ R#Error \033[0;37m] {i} has been not downloaded!!!'))
                    print(f'{tool.stderr.decode("utf-8")}')

            except KeyError:
                print(Color.reader(f'\033[0;37m[ R#Error \033[0;37m] {i} not found in tools db file!!!'))
        print(Color.reader('\nW#Done...'))
        os.chdir(XPATH+'N404-Tool')

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
