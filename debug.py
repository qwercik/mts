import sys

def print_stderr(*args, **kwargs):
    kwargs['file'] = sys.stderr
    print(*args, **kwargs)

def dbg(*args, **kwargs):
    print_stderr('[DBG]', *args, **kwargs)

def warning(*args, **kwargs):
    print_stderr('[WARNING]', *args, **kwargs)

def error(code, *args, **kwargs):
    print_stderr('[ERROR]', *args, **kwargs)
    sys.exit(code)
