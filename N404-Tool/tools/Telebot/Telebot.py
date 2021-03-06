from N4Tools.Design import (
    Color,Style,Animation
    )
from tools.root import (
HELP_TELEBOT as HELP,
OPTIONS_TELEBOT as OPTIONS,
SHELL_ALL,TOOLS_PATH,
XPATH,Errors,read_data,
save_data )

import telebot ,json ,os

class Telebot_shell(SHELL_ALL):
    # the shell command...
    page = 'Telebot'
    token = None
    database = None

    def __init__(self):
        super().__init__()
        _db = read_data(['Telebot'])
        if read_data(['Telebot','token']):
            self.token = _db['token']
            self.database = _db['file']

    def help(self):
        return  self.SQUARE(HELP)

    def data(self):
        with open(self.database,'r') as f:
            db = f.read()
        db = db.split(';')
        temp = []
        for i in db:
            temp.append(i.split('"'))
        db = {}
        for i in temp:
            try:
                test = i[4]
                db[i[1]] = {'msg':i[3],'type':i[4].strip()}
            except IndexError:
                pass
        return db

    def save(self):
            save_data({'Telebot':{'token':self.token,'file':self.database}})

    def do_start(self,arg):
        if self.token and self.database and os.path.isfile(self.database):
            bot = telebot.TeleBot(token=self.token)
            @bot.message_handler(func=lambda m: True)
            def Read_messages(msg):
                try:
                    db=self.data()[msg.text]
                    if db['type'] == '#send':
                        bot.send_message(msg.chat.id,text=db['msg'])
                    elif db['type'] == '#reply':
                        bot.reply_to(msg,db['msg'])
                    print (Color.reader(f'W#[ G#msg W#] send to {msg.chat.id}'))
                except KeyError:
                    print (Color.reader(f'W#[ R#msg W#] not found in database!'))
            print (Color.reader('Y#bot C#: W#started successfully...'))
            bot.polling(none_stop=True)
            print (Color.reader('\rY#bot C#: W#stopped successfully...'))
        else:
            print('Error: value not found')

    def do_EOF(self,arg):
        print (Color.reader('\nY#bot C#: W#killed successfully...'))

    def do_options(self,arg):
        op = self.SQUARE(OPTIONS.format(
        token=self.token,
        database=self.database,
        ))
        print (op)

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
        if name == 'token':
            self.token = set
            self.save()
        elif name == 'database':
            if os.path.isfile(os.path.join(os.getcwd(),set)) :
                self.database = os.path.join(os.getcwd(),set)
                self.save()
            elif os.path.isfile(set):
                self.database = set
                self.save()
            else:
                NoError = False
                print(Errors['NotExist'].format(set))
        else:
            NoError = False
            print(Color.reader(f'Error: {name}: command not found'))

        print (Color.reader(f'Y#{arg[0]} C#: W#{set}\n') if NoError else '',end='')

    def complete_set(self, text, line, begidx, endidx):
        comp = ['token','database']
        if not text:
            return comp[:]
        else:
            return [_ for _ in comp if _.startswith(text)]
if __name__=='__main__':
    Telebot_shell
