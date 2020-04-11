#!/usr/bin/python
from cmd import Cmd
from My_Style import Color,Style,Animation
import os ,sys
from tools import Tools_shell

HELP ='''
             Y#N404-Tool R#vB#{C#1.0B#}

 sections:
-------------------------------------------
  Tools     There are more than 200 tools.
  Style     Create your own style.
  Hash      New and complex encryption.
  Fishing   Hack through fake pages.
  Telebot   Create your own telegram bot.
-------------------------------------------

 system:
-------------------------------------------
  clear      clear the screen.
  exit       stop the Tool.
  Update     update N404-Tool
  About      about us
-------------------------------------------
'''
Color.Theme('light')

def intro_text(type=True):
    S = 'G#[Y#+G#]'
    if type:
        return Style(HELP).Square(
        Square=[S,' G#| ',S,'-',S,' G#|',S,'-'])
    else:
        Animation.SlowLine( Style(HELP).Square(
        Square=[S,' G#| ',S,'-',S,' G#|',S,'-']
        ),t=0.03)

class shell(Cmd):
    prompt = Color.reader(f'G#┌───B#[ C#{os.uname().sysname}B# ]G##B#[ Y#{os.uname().nodename} B#]G##B#[ R#No Name B#]G#>>>\nG#|\nG#└─>>>$ W#')
    intro = intro_text()

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

    def do_Tools(self,arg):
        Tools_shell.shell_main = super(shell,self).cmdloop
        Tools_shell().cmdloop(Tools_shell().help())

    def do_Chat(self,arg):
        Chat_shell().cmdloop(self.prompt.replace('No Name', 'Chat'))

    def do_Style(self,arg):
        Style_shell().cmdloop(self.prompt.replace('No Name', 'Style'))

    def do_Hash(self,arg):
        Hash_shell().cmdloop(self.prompt.replace('No Name', 'Hash'))

    def do_Fishing(self,arg):
        Fishing_shell().cmdloop(self.prompt.replace('No Name', 'Fishing'))

    def do_Ddos(self,arg):
        Ddos_shell().cmdloop(self.prompt.replace('No Name', 'Ddos'))

    def do_Telebot(self,arg):
        Telebot_shell().cmdloop(self.prompt.replace('No Name', 'Telebot'))

if __name__=='__main__':
    shell().cmdloop()
