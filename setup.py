#!/usr/bin/python3 -B
import os,sys,subprocess
from distutils.spawn import find_executable
is_exist = lambda text:True if find_executable(
                            str(text)) else False

if 'com.termux' in os.getcwd():
    DEL = 'rm -rif '
    install = 'pkg install'
    root = ''
    MV = 'mv '
    chmod = 'chmod 777 '
    python = 'pkg install python'
else:
    DEL = 'sudo rm -rif '
    MV = 'sudo mv '
    install = 'apt-get install'
    root = 'sudo '
    chmod = 'sudo chmod 777 '
    python = 'sudo apt-get install python3'

class setup:
    test = {
    }
    tools = {
        'figlet':root+install+' figlet',
        'toilet':root+install+' toilet',
        'pip3':root+install+' python3-pip',
        'python3':python,
    }

    libs = {
        'flask':root+'pip3 install flask',
        'flask_ngrok':root+'pip3 install flask_ngrok',
        'My_Style':root+'pip3 install My_Style',
        'requests':root+'pip3 install requests',
        'telebot':root+'pip3 install pyTelegramBotAPI',
    }
    def run(self):
        print ('please wait...')
        self.shell()
        self.module()
        print (os.getcwd())
    #    self.setup()

    def setup(self):
        subprocess.run(DEL+os.environ['SHELL'].replace('bash', 'N404-Tool'),shell=True,capture_output=True)
        subprocess.run(MV+'N404-Tool/N404-Tool '+os.environ['SHELL'].replace('bash', ''),shell=True,capture_output=True)
        subprocess.run(chmod+os.environ['SHELL'].replace('bash', 'N404-Tool'),shell=True,capture_output=True)
        subprocess.run(DEL+os.environ['SHELL'].replace('bin/bash', 'lib/N404-Tool'),shell=True,capture_output=True)
        subprocess.run(MV+'N404-Tool '+os.environ['SHELL'].replace('bin/bash', 'lib/'),shell=True,capture_output=True)
        subprocess.run(DEL+(os.getcwd() if os.getcwd().endswith('-Tool') else os.getcwd()+'/N404-Tool' ),shell=True,capture_output=True)

    def shell(self):
        for name,shell in self.tools.items():
            subprocess.run(shell+' -y',shell=True)

        print ('\nChecking...')
        for name in self.tools:
            if is_exist(name):
                print (f'\033[0;37m[ \033[1;32mOK\033[0;37m ] {name} has been installed...')
                self.test[name] = True
            else:
                print (f'\033[0;37m[ \033[1;31mError\033[0;37m ] {name} has not been installed !!!')
                self.test[name] = False

    def module(self):
        for name,lib in self.libs.items():
            try:
                exec(f'import {name}')
                print (f'\033[0;37m[ \033[1;32mOK\033[0;37m ] {name} has been installed...')
            except ModuleNotFoundError:
                check = subprocess.run(lib,shell=True,capture_output=True)
                if check.stderr.decode('utf-8') == '':
                    print (f'\033[0;37m[ \033[1;32mOK\033[0;37m ] {name} has been installed...')
                    self.test[name] = True
                else:
                    print (f'\033[0;37m[ \033[1;31mError\033[0;37m ] {name} has not been installed !!!')
                    self.test[name] = False

if __name__=='__main__':
    setup = setup()
    setup.run()
