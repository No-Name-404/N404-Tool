#!/usr/bin/python3 -B
import os,sys,subprocess
from distutils.spawn import find_executable
is_exist = lambda text:True if find_executable(
                            str(text)) else False

if 'com.termux' in os.getcwd():
    DEL = 'rm -rif '
    MV = 'mv '
    install = 'pkg install'
    root = ''
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
        'N4Tools':root+'pip3 install N4Tools',
        'requests':root+'pip3 install requests',
        'six':root+'pip3 install six',
        'chardet':root+'pip3 install chardet',
        'urllib3':root+'pip3 install urllib3',
        'certifi':root+'pip3 install certifi',
        'idna':root+'pip3 install idna'
        'telebot':root+'pip3 install pyTelegramBotAPI',
    }
    def run(self):
        print ('please wait...')
        self.shell()
        self.module()
        self.setup()
        self.Check()

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
        subprocess.run('pip3 install --upgrade pip',shell=True)

        for name in self.tools:
            if is_exist(name):
                self.test[name] = True
            else:
                self.test[name] = False

    def module(self):
        for name,lib in self.libs.items():
            subprocess.run(lib,shell=True)

        for name,lib in self.libs.items():
            try:
                exec(f'import {name}')
                self.test[name] = True
            except ModuleNotFoundError:
                self.test[name] = False

    def Check(self):
        print ('\nChecking...')
        for name,check in self.test.items():
            if check:
                print (f'\033[0;37m[ \033[1;32mOK\033[0;37m ] {name} has been installed...')
            else:
                print (f'\033[0;37m[ \033[1;31mError\033[0;37m ] {name} has not been installed !!!')
            time.sleep(0.5)
        if len(sys.argv) > 1 and all([_ for x,_ in self.test.items()]):
            print (f'\033[0;37m[ \033[1;32mOK\033[0;37m ] N404-Tool has been installed ')
            print (f'To get start type \033[1;33mN404-Tool\033[0;37m')
        else:
            print (f'\033[0;31mThere are some problems that you must solve')
            for name,check in self.test.items():
                if chack:
                    pass
                else:
                    try:
                        print ('\033[0;37m'+name,'"\033[0;33m'+self.tools[name]+'\033[0;37m"')
                    except:
                        print ('\033[0;37m'+name,'"\033[0;33m'+self.libs[name]+'\033[0;37m"')

if __name__=='__main__':
    setup = setup()
    setup.run()
