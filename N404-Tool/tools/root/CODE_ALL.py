import os, textwrap, shutil, subprocess
from cmd import Cmd

from N4Tools.Design import Color,Style,Animation
from tools.root.db import (
Errors,RULER_UOT,
save_data,read_data)

Color.Theme('light')

# os.uname().sysname
# DESIGN and CODE - ALL TOOL...
PROMPT = lambda text,pwd:Color.reader(f'G#┌───B#[ C#{pwd}B# ]G##B#[ Y#{os.uname().nodename} B#]G##B#[ R#{text} B#]G#>>>\nG#│\nG#└─>>>W#$ \033[0;37m')

class SHELL_ALL(Cmd):
    page = 'main'
    shell_main = None
    path = os.environ['HOME'] # user path (home or root)
    tool_path = os.getcwd()

    def __init__(self):
        super(SHELL_ALL,self).__init__()
        self.intro = self.help()
        self.prompt = PROMPT(self.page,os.getcwd().split("/")[-1])

    def get_terminal_size(self):
        return shutil.get_terminal_size().columns

    def SQUARE(self,HELP,type=True): # Tool DESIGN
        S = 'G#[Y#+G#]'
        if type:
            return Style(HELP).Square(
            Square=[S,' G#│ ',S,'─',S,' G#│',S,'─'])
        else:
            os.system('clear')
            Animation.SlowLine(HELP,t=0.01)

    def cmdloop(self,*arg,**kwargs):
        try:
            super().cmdloop(*arg,**kwargs)
        except KeyboardInterrupt: # if user click (ctrl + c)
            print('\n\033[0m')
            exit()

    def default(self, line):
        '''
        if user enter a wrong command,
        this message will be display
        '''
        if read_data(['root','bash']) == 'N4all':
            os.system(line)
        else:
            print('bash: %s: command not found'%line)

    def do_clear(self,arg):
        os.system('clear')

    def do_exit(self,arg):
        exit('\033[0m')

    def do_bash(self,arg):
        if arg == 'N4all':
            save_data({'root':{'bash':arg}})
            print (Color.reader('G## The tool now supports bash \n# Done'))
        elif arg == 'N4not':
            save_data({'root':{'bash':arg}})
            print (Color.reader('G## The tool now not supports bash \n# Done'))
        else:
            os.system(arg)

    def do_cat(self,arg):
        try:
            with open(os.path.join(os.getcwd(),arg),'rb') as f:
                file = f.read().decode('utf-8')
            print (file[0:-1] if file.endswith('\n') else file)
        except UnicodeDecodeError as U:
            print (U)
        except FileNotFoundError as F:
            print (Errors['FileNotFoundError'].format(arg))
        except IsADirectoryError:
            print(Errors['IsADirectoryError'].format(arg))

    def do_ls(self,arg):
        path = os.getcwd()
        files = os.popen('ls').read()
        files = files.split('\n')
        output = ''
        for i in files:
            if os.path.isfile(os.path.join(path,i)):
                if i.endswith('.png') or i.endswith('.jpg'):
                    output += '\033[1;95m'+i+' '
                else:
                    output += '\033[0;37m'+i+' '
            elif os.path.isdir(os.path.join(path,i)):
                output += '\033[1;34m'+i+' '
            else:
                output += i
        output = output[0:-8].split(' ')
        self.columnize(output,displaywidth=self.get_terminal_size())

    def do_cd(self,arg):
        try:
            if arg in ['~','$HOME','']:
                os.chdir(os.environ['HOME'])
            else:
                os.chdir(os.path.join(os.getcwd(),arg))
            self.prompt = PROMPT(self.page,os.getcwd().split("/")[-1])
        except FileNotFoundError:
            print (Errors['FileNotFoundError'].format(arg))
        except NotADirectoryError:
            print (Errors['NotADirectoryError'].format(arg))

    def do_pwd(self,arg):
        print(os.getcwd())

    def do_rm(self,arg):
        os.system('rm '+arg.strip())

    def do_run(self,arg):
        data = {
        '.py':'python3',
        '.pyc':'python3',
        '.sh':'bash',
        '.php':'php',
        '.js':'node',
        '.md':'cat',
        '.txt':'cat',
        }
        if os.path.isfile(os.path.join(os.getcwd(),arg)):
            Error = False
            for end,code in data.items():
                if arg.endswith(end):
                    os.system(code+' '+arg)
                    Error = False
                    break
                else:
                    Error = True
            if Error:
                print('can not read this file.')
        else:
            print(f'Error: {arg}: not exist')


    def do_help(self,arg):
        if arg: # check if run as intro
            super().do_help(arg) # display help text
        else:
            self.SQUARE(self.help(),type=False) # display help text as Animation

    def help(self):
        return 'text'

    def do_main(self,arg):
        try:
            os.system('clear')
            self.shell_main()
        except TypeError:
            print ('This is the Main page...')

    # complete files name ...
    def completeFiles(self,text):
        files = os.popen('ls').read().split('\n')
        if not text:
            completions = files[:-1]
        else:
            completions = [
                f
                for f in files
                if f.startswith(text)
            ]
        return completions

    def complete_rm(self,*args):
        return self.completeFiles(args[0])

    def complete_cat(self,*args):
        return self.completeFiles(args[0])

    def complete_cd(self,*args):
        return self.completeFiles(args[0])

    def complete_run(self,*args):
        return self.completeFiles(args[0])

    def complete_bash(self,*args):
        return self.completeFiles(args[0])

class EasyCmd:
    def __init__(self):
        if 'com.termux' in os.getcwd():
            self.bash_file = os.environ['PREFIX']+'/etc/bash.bashrc'
            self.shell = 'pkg '
            self.text = '''
# From N404-Tool...
alias i='pkg install'
alias g='git clone'
alias c='clear'
alias p3='python3'
alias p2='python2'
alias p='python'
alias b='bash'
alias r='rm -rif'
alias u='pkg update && pkg upgrade'
alias x='exit'
alias h='cd ~'
# end...
'''
        else :
            self.bash_file = '/etc/bash.bashrc'
            self.shell = 'apt-get '
            self.text = '''
# From N404-Tool...
alias i='sudo apt-get install'
alias g='git clone'
alias c='clear'
alias p3='sudo python3'
alias p2='sudo python2'
alias b='sudo bash'
alias r='sudo rm -rif'
alias u='sudo apt-get update && sudo apt-get upgrade'
alias x='exit'
alias d='cd ~/Desktop/'
# end...
'''
    def write(self):
        with open(self.bash_file,'r') as f:
            file = f.read()
        if os.path.isfile(self.bash_file):
            if self.text not in file:
                with open(self.bash_file,'a') as f:
                    f.write(self.text)
            self.end()
        else:
            print (Color.reader('R#Error...\nThe W#bash.bashrc R#file not found'))

    def end(self):
        info = self.text.split("alias ")
        temp = {}
        for i in info:
            try:
                temp[i.split('=')[0]]=i.split('=')[1].replace("'","")
            except IndexError:
                pass
        info = f'\n\033[0m commands:\n{RULER_UOT}\n'
        for x,y in temp.items():
            y = y.replace('\n# end...','')
            if len(x) == 2:
                info += f'  Y#{x}C#: P#{y}\033[0m'
            elif len(x) == 1:
                info += f'  Y#{x} C#: P#{y}\033[0m'
        print (Color.reader(info+RULER_UOT+'\n'))
