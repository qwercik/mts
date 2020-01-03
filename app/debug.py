import sys
import io
from termcolor import colored
from app.utilities import printToString

INFO_COLOR = 'cyan'
WARNING_COLOR = 'magenta'
ERROR_COLOR = 'red'

def printStderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def printStderrColor(color, *args, **kwargs):
    print(colored(printToString(*args, **kwargs), color))

def info(*args, **kwargs):
    printStderrColor(INFO_COLOR, '[INFO]', *args, **kwargs)

def warning(*args, **kwargs):
    printStderrColor(WARNING_COLOR, '[WARNING]', *args, **kwargs)

def error(*args, **kwargs):
    printStderrColor(ERROR_COLOR, '[ERROR]', *args, **kwargs)

def panic(code, *args, **kwargs):
    error(*args, **kwargs)
    sys.exit(code)
