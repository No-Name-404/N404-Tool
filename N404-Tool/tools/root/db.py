import shutil

terminal_size = shutil.get_terminal_size().columns
RULER = '╌'*(terminal_size-6)

# Errors...
Errors={
'FileNotFoundError':'bash: cd: {}: No such file or directory',
'NotADirectoryError':'bash: cd: {}: Not a directory',
'IsADirectoryError':'cat: {}: Is a directory',
}

# TOOL ...
NEW_TOOL = f'''
 New:
{RULER}
  EasyCmd has been added..
  Fix errors [path , database , install]
  The Fishing section has been deleted...
{RULER}

 To use:
{RULER}
  N404-Tool EasyCmd
{RULER}
'''

HELP_TOOL = f'''
 N404-Tool:
{RULER}
  Tools     To open Tools section.
  Style     To open Style section.
  Hash      To open Hash section.
  Telebot   To open Telebot section.
  Password  To open Password section.
{RULER}
  EasyCmd   Shortcuts to commands.
  Update    To update the tool.
{RULER}
  New       What is the New ?
{RULER}
'''

# main shell texts...
HELP_MAIN ='''
***SPACE***Y#N404-Tool R#vB#{C#1.0B#}

 sections:
***RULER***
  Tools     There are more than 200 tools.
  Style     Create your own style.
  Hash      New and complex encryption.
  Telebot   Create your own telegram bot.
  password  To create list of passwords.
***RULER***

 system:
***RULER***
  clear      Clear the screen.
  exit       Stop the Tool.
  bash       e.g ( bash ls ).
  run        e.g ( run a.py or a.sh or...)

  cat        read files.
  ls         show file and folder.
  cd         open folder.
  rm         delete files.
  pwd        show the path.

  update     To update N404-Tool.
  delete     To delete N404-Tool!!.
  about      About the developer.
***RULER***
'''.replace('***RULER***', RULER).replace('***SPACE***', ' '*(((terminal_size-6)//2)-7))

ABOUT_MAIN = '''
 about:
***RULER***
  name      Mohamed Al-kainai.
  age       5-11-2002.
  country   Yemen.
  telegram  @No_Name_N4
  support   C#https://bit.ly/2Kmc2Bs
  youtube   C#https://bit.ly/3b3uPwV
***RULER***
'''.replace('***RULER***', RULER)

# Tools shell texts...
HELP_TOOLS ='''
 sections:
***RULER***
  show       To display the tools.
  options    Display the options menu.
  download   To download the tools.
  main       main page.
***RULER***
'''.replace('***RULER***', RULER)

OPTIONS_TOOLS = '''
 options:
***RULER***
  path : {}
***RULER***
'''.replace('***RULER***', RULER)

# Style shell texts...
HELP_STYLE ='''
 sections:
***RULER***
  options    Display the options menu.
  show       To show the design.
  save       To save the design.
  main       main page.
***RULER***

 note:
***RULER***
  Red    : RR##
  Green  : GG##
  Yellow : YY##
  Blue   : BB##
  Cyan   : CC##
  Purple : PP##
  White  : WW##

# You can use these symblos to color text.
***RULER***
'''.replace('***RULER***', RULER)

OPTIONS_STYLE = '''
 options:
***RULER***
  intro : {Intro}
  title : {title}
  tools :
 ------------------
{tools}
 ------------------
  padding_x : {padding_x}
  padding_y : {padding_y}
  path : {path}
  file : {file}
***RULER***
'''.replace('***RULER***', RULER)

# Hash shell texts...
HELP_HASH = '''
 sections:
***RULER***
  options    Display the options menu.
  start      to start hashing.
  main       main page.
***RULER***
'''.replace('***RULER***', RULER)

OPTIONS_HASH = '''
 options:
***RULER***
  type : {type}
  path : {file_or_folder}
  copy : {copy}
***RULER***
'''.replace('***RULER***', RULER)

# Telebot shell texts...
HELP_TELEBOT = '''
 sections:
***RULER***
  options    Display the options menu.
  start      To start the bot server.
  main       Main page.
***RULER***
'''.replace('***RULER***', RULER)
OPTIONS_TELEBOT = '''
 options:
***RULER***
  token : {token}
  database : {database}
***RULER***
'''.replace('***RULER***', RULER)

#
HELP_PASSWORD ='''
 sections:
***RULER***
  options    Display the options menu.
  start      To start the counter.
  main       Main page.
***RULER***
'''.replace('***RULER***', RULER)
OPTIONS_PASSWORD = '''
 options:
***RULER***
  type : {type} R## text or numder
  list : {list}
***RULER***
'''.replace('***RULER***', RULER)
