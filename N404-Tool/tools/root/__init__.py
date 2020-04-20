from .CODE_ALL import SHELL_ALL,PROMPT
from .db import *
from os import path
import tools, sys

TOOLS_PATH = path.abspath(tools.__file__).replace('__init__.py', '')
XPATH = path.abspath(tools.__file__).replace('N404-Tool/tools/__init__.py', '')
#sys.path += [TOOLS_PATH]
