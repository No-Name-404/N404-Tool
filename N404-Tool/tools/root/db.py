RULER = '-'*43

# main shell texts...
HELP_MAIN ='''
             Y#N404-Tool R#vB#{C#0.6B#}

 sections:
***RULER***
  Tools     There are more than 200 tools.
  Style     Create your own style.
  Hash      New and complex encryption.
  Fishing   Hack through fake pages.
  Telebot   Create your own telegram bot.
***RULER***

 system:
***RULER***
  clear      Clear the screen.
  exit       Stop the Tool.
  update     To update N404-Tool.
  about      About the developer.
***RULER***
'''.replace('***RULER***', RULER)

ABOUT_MAIN = '''
 about:
***RULER***
  name      Mohamed Al-kainai.
  age       5-11-2002.
  country   Yemen.
  telegram  @N404_No_Name_404_N4
  support   C#https://paypal.me/Mohamedkainai
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
***RULER***
'''.replace('***RULER***', RULER)

# Fishing shell texts...
HELP_FISHING = '''
 sections:
***RULER***
  options    Display the options menu.
  start      To start the Server.
  main       Main page.
***RULER***
'''.replace('***RULER***', RULER)
OPTIONS_FISHING = '''
 options:
***RULER***
  server : {server}
  page : {page}
***RULER***
'''.replace('***RULER***', RULER)
