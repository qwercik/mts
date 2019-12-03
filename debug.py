import sys
from termcolor import colored

INFO_COLOR = 'cyan'
WARNING_COLOR = 'magenta'
ERROR_COLOR = 'red'

def print_stderr(*args, **kwargs):
    kwargs['file'] = sys.stderr
    print(*args, **kwargs)

def info(message):
    print_stderr(colored('[INFO] ' + message, INFO_COLOR))

def warning(message):
    print_stderr(colored('[WARNING] ' + message, WARNING_COLOR))

def error(message, code):
    print_stderr(colored('[ERROR] ' + message, ERROR_COLOR))
    sys.exit(code)
