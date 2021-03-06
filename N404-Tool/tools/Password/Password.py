from N4Tools.Design import (
    Color,Style,Animation
    )
from tools.root import (
HELP_PASSWORD as HELP,
OPTIONS_PASSWORD as OPTIONS,
SHELL_ALL,Errors)

import os

class LIST:
    def __init__(self,list='1000',file='list.txt'):
        self.list = list.strip()
        self.file = file
        self.type = None
        self._check()

    def run(self):
        if self.type == 'int':
            self.int_list()
        elif self.type == 'info':
            self.info_list()
        else :
            self.str_list()

    def _check(self):
        try:
            temp = int(self.list)
            self.type = 'int'
            return True
        except:
            if self.list.startswith('<') and self.list.endswith('>'):
                self.type = 'info'
                return True
            else:
                if len(self.list) <= 9 :
                    self.type = 'str'
                    return True
                else:
                    return False

    def clear_file(self):
        with open(self.file,'w') as f:
            f.write('')

    def write_file(self,text):
        with open(self.file,'a') as f:
            f.write(text)

    def int_list(self):
        self.clear_file()
        nums = len(self.list)
        temp = 0
        counter = 0
        print (Color.reader(f'G## Loading B#[ W#0 B#% W#100 B#]'),end='\r')
        for i in range(int(self.list)):
            i += 1
            temp += 1
            password = f"{'0'*(nums-len(str(i)))}{i}\n"
            self.write_file(password)
            if int(self.list)//100 == temp:
                counter += 1
                print (Color.reader(f'G## Loading B#[ W#{counter if counter < 100 else 100} B#% W#100 B#]'),end='\r')
                temp = 0
            elif int(self.list) < 100:
                print (Color.reader(f'G## Loading B#[ W#100 Y#% W#100 B#]'),end='\r')
        print (Color.reader(f'\nG## Was created {self.list} passwords\n# Dane...'))

    def str_list(self):
        self.clear_file()
        nums = eval(f'{"{}*".format(len(self.list))*len(self.list)}'[:-1])
        temp = 0
        counter = 0
        print (Color.reader(f'G## Loading B#[ W#0 B#% W#100 B#]'),end='\r')
        for password in self.mix():
            temp += 1
            self.write_file(password+'\n')
            if nums//100 == temp:
                counter += 1
                print (Color.reader(f'G## Loading B#[ W#{counter if counter < 100 else 100} B#% W#100 B#]'),end='\r')
                temp = 0
            elif nums < 100:
                print (Color.reader(f'G## Loading B#[ W#100 Y#% W#100 B#]'),end='\r')
        print (Color.reader(f'\nG## Was created {nums} passwords\n# Dane...'))

    def info_list(self):
        self.clear_file()
        list = self.list[1:-1].split('-')
        nums = eval(f'{"{}*".format(len(list))*len(list)}'[:-1])
        temp = 0
        counter = 0
        print (Color.reader(f'G## Loading B#[ W#0 B#% W#100 B#]'),end='\r')
        for password in self.mix(text=[[_ for _ in list]]*len(list),list=list):
            temp += 1
            self.write_file(password+'\n')
            if nums//100 == temp:
                counter += 1
                print (Color.reader(f'G## Loading B#[ W#{counter if counter < 100 else 100} B#% W#100 B#]'),end='\r')
                temp = 0
            elif nums < 100:
                print (Color.reader(f'G## Loading B#[ W#100 Y#% W#100 B#]'),end='\r')
        print (Color.reader(f'\nG## Was created {nums} passwords\n# Dane...'))

    def mix(self,text=False,list=False):
        if not text:
            text = [[_ for _ in self.list]]*len(self.list)
        if not list:
            list = self.list
        for a in text[0]:
            if len(list) == 1: #2
                yield a
            else:
                for b in text[1]:
                    if len(list) == 2: #2
                        yield a+b
                    else:
                        for c in text[2]:
                            if len(list) == 3: #3
                                yield a+b+c
                            else:
                                for d in text[3]:
                                    if len(list) == 4: #4
                                        yield a+b+c+d
                                    else:
                                        for e in text[4]:
                                            if len(list) == 5: #5
                                                yield a+b+c+d+e
                                            else:
                                                for f in text[5]:
                                                    if len(list) == 6: #6
                                                        yield a+b+c+d+e+f
                                                    else:
                                                        for g in text[6]:
                                                            if len(list) == 7: #7
                                                                yield a+b+c+d+e+f+g
                                                            else:
                                                                for h in text[7]:
                                                                    if len(list) == 8: #8
                                                                        yield a+b+c+d+e+f+g+h
                                                                    else:
                                                                        for i in text[8]:
                                                                            yield a+b+c+d+e+f+h

class Password_shell(SHELL_ALL):
    # the shell command...
    page = 'Password'
    file = 'N4list.txt'
    list = None

    def __init__(self):
        super().__init__()

    def help(self):
        return self.SQUARE(HELP)

    def do_options(self,arg):
        op = OPTIONS.format(file=self.file, list='None R## text or numder' if self.list == None else self.list )
        print (self.SQUARE(op))

    def do_set(self,arg):
        arg = arg.strip().split(' ')
        name = arg[0].strip() # name set...
        NoError = True
        try:
            '''
            if the user set value else
            return error.
            '''
            set = arg[1].strip() # values
        except:
            NoError = False
            set = None
            name = None
            print('Error: value not found')
        if name == 'list':
            if LIST(list=set)._check() and set != '':
                self.list = set
            else:
                NoError = False
                print (f'Error: {set}: is greater than 9')

        elif name == 'file':
            if not os.path.isfile(os.path.join(os.getcwd(),set)) :
                self.file = os.path.join(os.getcwd(),set)
            elif not os.path.isfile(set):
                self.file = set
            else:
                NoError = False
                print(Errors['IsAlreadyExist'].format(set))
        else:
            NoError = False
            print(Color.reader(f'Error: {name}: command not found'))
        print (Color.reader(f'Y#{arg[0]} C#: W#{set}\n') if NoError else '',end='')

    def complete_set(self, text, line, begidx, endidx):
        comp = ['list','file']
        if not text:
            return comp[:]
        else:
            return [_ for _ in comp if _.startswith(text)]

    def do_start(self, arg):
        if self.file and self.list:
            LIST(list=self.list,file=self.file).run()
        else:
            print('Error: value not found')
