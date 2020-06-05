from N4Tools.Design import (
    Color,Style,Animation
    )
import os ,sys ,base64 ,marshal ,py_compile ,time

from tools.root import (
HELP_HASH as HELP,
OPTIONS_HASH as OPTIONS,
PROMPT,
SHELL_ALL,
TOOLS_PATH,
XPATH )

class hashing:
    A = '#!/usr/bin/python3 -B\n'
    def __init__(self,file_or_folder,type,copy):
        self.path = os.path.join(os.getcwd(),file_or_folder)
        self.check = self.check_type()
        self.copy = copy
        if type == 'md5':
            self.md5()
        elif type == 'marshal':
            self.marshal()
        elif type == 'pyc':
            self.pyc()
        elif type == 'malker':
            print ('soon...')
        print ('Done...')

    def name_file(self,file,text):
        if self.copy:
            if file.endswith('.py'):
                return file[0:-2]+text
            else:
                return file+'.'+text
        elif self.copy == False:
            return file

    def check_type(self):
        o = os.path
        if o.isdir(self.path) or o.isfile(self.path):
            if o.isdir(self.path):
                return 'folder'
            elif o.isfile(self.path):
                return 'file'
        else:
            return False

    def get_files(self):
        files = []
        if self.check == 'folder':
            for d,r,f in os.walk(self.path):
                for i in f:
                    if os.path.join(d,i).endswith('.py'):
                        files.append(os.path.join(d,i))
        return files

    def msg(self,name):
        name = name.split('/')[-1]
        print (Color.reader(f'Y#start hashingW#...R#[B# {name} R#]'))
        time.sleep(0.6)

    def md5(self):
        def encode(path):
            self.msg(path)
            with open(path,'rb') as f:
                rb_file = base64.b16encode(f.read())
            with open(self.name_file(path, 'md5'),'w') as f:
                f.write(f"{self.A}import base64 as b\ndata = lambda x: x({rb_file})\nexec (compile(data(b.b16decode),'<N404-Tools>','exec'))")
        if self.check == 'file':
            encode(self.path)
        if self.check == 'folder':
            for i in self.get_files():
                encode(i)

    def marshal(self):
        def encode(path):
            self.msg(path)
            with open(path,'r') as f:
                r_file = compile(f.read(),'<N404-Tool>','exec')
                r_file = marshal.dumps(r_file)
            with open(self.name_file(path, 'marshal'),'w') as f:
                f.write(f"{self.A}import marshal as m\ndata = m.loads({r_file})\nexec (data)")
        if self.check == 'file':
            encode(self.path)
        if self.check == 'folder':
            for i in self.get_files():
                encode(i)

    def pyc(self):
        def encode(source_path):
            self.msg(source_path)
            basename = source_path[:-3]
            bytecode_path = "%s.pyc" % (basename)
            py_compile.compile(source_path, bytecode_path, "exec")
            if self.copy == False:
                os.system('rm '+source_path)
            return bytecode_path
        if self.check == 'file':
            encode(self.path)
        if self.check == 'folder':
            for i in self.get_files():
                encode(i)

    def malker(self):
        def encode(path):
            self.msg(path)
            text = ''
            with open(path,'r') as f:
                r_file = f.read()
            for _ in r_file.split('\n'):
                for i in _:
                    if i != ' ' and '\n':
                        try:
                            text += chr(ord(i)+31227)
                        except:
                            text += i
                    else:
                        text += i
                text += '\n'
            with open(path[0:-2]+'malker','w') as f:
                f.write('#!/usr/bin/malker\n'+text)
        if self.check == 'file':
            encode(self.path)
        if self.check == 'folder':
            for i in self.get_files():
                encode(i)

class Hash_shell(SHELL_ALL):
    # the shell command...
    page = 'Hash'
    # prompt = PROMPT('Hash')
    file_or_folder = None
    type = None
    PATH_H = os.getcwd()+'/'
    copy = False
    # path from SHELL_ALL class

    def help(self):
        return  self.SQUARE(HELP)

    def do_options(self,arg):
        # to set the color of the hash type...
        type = Color.reader('Y#{ ')
        for i in ['pyc','md5','marshal']:
            if self.type == i:
                type += Color.reader(f'G#{i}W# ')
            else:
                type += Color.reader(f'W#{i} ')
        type += Color.reader('Y#}')
        # to display the option msg...
        op = OPTIONS.format(
        type=type,
        file_or_folder=self.file_or_folder,
        copy=self.copy,
        )

        op = self.SQUARE(op)
        print(op)

    def do_start(self,arg):
        # start hashing...
        if self.file_or_folder and self.type:
            hashing(self.file_or_folder,self.type,self.copy)
        else:
            print ('Error: value not found')

    def do_set(self,arg):
        arg = arg.strip().split(' ')
        name = arg[0].strip() # name set...
        OP_H = ['pyc','md5','malker','marshal']
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
        if name == 'type':
            if set in OP_H:
                self.type = set
            else:
                NoError = False
                print(f'Error: {set}: type hash not found')
        elif name == 'path':
            if os.path.isfile(os.path.join(self.PATH_H,set)) and os.path.join(self.PATH_H,set).endswith('.py'):
                self.file_or_folder = set
            elif os.path.isdir(os.path.join(self.PATH_H,set)):
                self.file_or_folder = set
            elif os.path.isfile(set) or os.path.isdir(set):
                self.file_or_folder = set
            else:
                NoError = False
                print(f'path: {set}: not exist')
        elif name == 'copy':
            if set == 'True':
                self.copy = True
            elif set == 'False':
                self.copy = 'False'
            else:
                NoError = False
                Color.Theme('dark')
                print(Color.reader(f'Error: {name}: set [ G#True W#or R#FalseW# ]'))
                Color.Theme('light')
        else:
            NoError = False
            print(Color.reader(f'Error: {name}: command not found'))
        print (Color.reader(f'Y#{arg[0]} C#: W#{set}\n') if NoError else '',end='')

    def complete_set(self,*args):
        OP = ['type','path']
        OP_H = ['pyc','md5','malker','marshal']
        if not args[0]:
            return OP[:]
        elif args[0]:
            if len(args[1].split(' ')) > 2 and 'type' in args[1]:
                return [_ for _ in OP_H if _.startswith(args[0])]
            return [_ for _ in OP if _.startswith(args[0])]
        return ['']
