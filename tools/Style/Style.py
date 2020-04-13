from cmd import Cmd
from My_Style import (
    Color,Style,Animation,Text
    )
from My_Style.Library import ProFunctions
import os ,sys ,json ,time ,random

from tools.DATA import (
HELP_STYLE as HELP,
OPTIONS_STYLE as OPTIONS,
PROMPT,
SHELL_ALL,
)

Color.Theme('light')

# Colors...
_set_c = lambda color:Color.reader(color)
R,G,Y,B,P,C,W,Bl = [
        _set_c('R#'),
        _set_c('G#'),
        _set_c('Y#'),
        _set_c('B#'),
        _set_c('P#'),
        _set_c('C#'),
        _set_c('W#'),
        _set_c('Bl#'),
]

class MakeStyle:
    def __init__(self,intro,title,tools,padding_x,padding_y):
        self.intro = intro
        self.title = title
        self.tools = tools
        self.padding_x = padding_x
        self.padding_y = padding_y
        self._c = self.RandColor()

    def RandColor(self):
        '''
        With this function, Ican create
        colors randomly while avoiding
        color similarity.
        '''
        color = []
        temp = 0
        while True:
            title = random.choice([R,G,W,P,C,B,Y,Bl])
            color += [title]
            tools = random.choice([R,G,W,P,C,B,Y,Bl])
            if tools in color:
                temp += 1
            color += [tools]
            toolsnum = random.choice([R,G,W,P,C,B,Y,Bl])
            if toolsnum in color:
                temp += 1
            color += [toolsnum]
            toolslist = random.choice([R,G,W,P,C,B,Y,Bl])
            if toolslist in color:
                temp += 1
            color += [toolslist]
            if temp == 0:
                break
            temp = 0
            color = []
        return color

    def StyleText(self): # Style system...
        '''
        This is the final design.
        '''
        _c = self._c
        Intro = Text(self.intro).Figlet() if self.intro else False

        title = _set_c(self.title)+'\n'
        tools = [f'{_c[0]}{name} {_c[2]}[{_c[1]}{num+1}{_c[2]}]'
                for num ,name in enumerate(self.tools)]
        tools = ProFunctions().Equal(*tools)
        tools = title+self.my_tool(tools)

        text = Style(tools).Center()
        if Intro:
            text = Style(Intro,tools).Center()
        return text

    def my_square(self,tools,index,text):
        '''
        This function create 2 Squares...
        '''
        _c = self._c
        return Style(*tools[index:index+2]).Square(
        Square=['╔','╢','╚','═','╝','╟','╗','═'],
        cols=2,
        space=9,
        padding_y=self.padding_y,
        padding_x=self.padding_x,
        Color=_c[1],
        ).replace('══',text)

    def my_tool(self,tools):
        '''
        This function organiazes the values
        and make the design using 'my_square'
        function.
        '''
        _c = self._c
        S = ''
        text = '\n'
        temp = True
        for i in range(0,len(tools),2):
            if temp:
                S += self.my_square(tools,i,'╧╤')+text
                temp = False
            else:
                S += self.my_square(tools,i,'╤╧')+text
                temp = True
        return (S).replace(
        Color.reader(f' {_c[1]}╟         {_c[1]}╢'),
        Color.reader(f' {_c[1]}╟--[{_c[0]}###{_c[1]}]--╢'))

class Style_shell(SHELL_ALL):
    prompt = PROMPT('Style')

    # options...
    Intro = None
    tools = ['text']
    title = 'text'
    padding_x = 5
    padding_y = 1
    file = 'N404Style.py'

    # save the design...
    save = None

    def help(self):
        return self.SQUARE(HELP)

    def do_options(self,arg):
        TOOLS_SHOW = ''
        for i in self.tools: TOOLS_SHOW += (' '*4)+i+'\n'
        op = OPTIONS.format(
            Intro=self.Intro,
            tools=TOOLS_SHOW[0:-1],
            title=self.title,
            padding_x=self.padding_x,
            padding_y=self.padding_y,
            path=self.path,
            file=self.file,
            )

        self.SQUARE(self.SQUARE(op),type=False)

    def do_set(self,arg):
        args = arg
        arg = arg.split(' ')
        set = ''
        for i in arg[1:]:set += i+' '
        NoError = True
        PATH = args.replace('path','').strip()
        CHECK = os.path.isdir(PATH)

        try:
            if arg[0] == 'intro':
                self.Intro = set
            elif arg[0] == 'tools':
                NoError = False
                self.tools = set.strip().split(' ')
                set_tools = ' W#'.join(self.tools)
                print (Color.reader(f'Y#{arg[0]} C#: W#{set_tools}'))
            elif arg[0] == 'title':
                self.title = set
            if arg[0] == 'file' and not os.path.isfile(os.path.join(self.path,set.strip())) :
                self.file = set
            elif arg[0] == 'file' and os.path.isfile(os.path.join(self.path,set.strip())) :
                NoError = False
                print(f'FileNameError: {set}:The name already exist')

            try:
                if arg[0] == 'padding_x':
                    self.padding_x = int(set)
                elif arg[0] == 'padding_y':
                    self.padding_y = int(set)

            except ValueError:
                NoError = False
                print ('Error:',arg[0]+': it should be a number')

            if 'path' in args and CHECK:
                self.path = set.strip()
            elif 'path' not in args and not CHECK:
                pass
            else :
                NoError = False
                print(f'PathError: {PATH}: not exist')

            print (Color.reader(f'Y#{arg[0]} C#: W#{set}\n') if NoError else '',end='')

        except IndexError as Error:
            print ('Error:',Error)

    def complete_set(self, text, line, begidx, endidx):
        LIST = ['intro','tools','padding_x','padding_y','path','title','file']
        if not text:
            return LIST[:]
        else:
            return [
                f
                for f in LIST
                if f.startswith(text)
            ]

    def do_show(self,arg):
        my_style = MakeStyle(self.Intro,self.title,
        self.tools,self.padding_x,self.padding_y)
        my_style = my_style.StyleText()
        self.save = my_style
        print(my_style)

    def do_save(self,arg):
        style = self.save
        path_file = os.path.join(self.path,self.file)
        with open(path_file,'w') as f:
            f.write(f'# from My_Style import Animation as An\ndef style():\n\treturn {bytes(style,"utf-8")}.decode(\'utf-8\')\n# To show...\n# print (style())\n# An.SlowLine(style(),t=0.02)')
            print (Color.reader(f'G#Done: B#{path_file}'))

if __name__ == '__main__':
    Style_shell().cmdloop()
    # s = MakeStyle('My Tools','R#title',['tools']*10,0,1)
    # print(s.StyleText())
