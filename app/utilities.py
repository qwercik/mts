import io

def popSeveral(inputList, count):
    data = inputList[-count:]
    inputList[-count:] = []
    
    if len(data) != count:
        raise IndexError('Tried to pop too many elements')

    return data

def printToString(*args, **kwargs):
    stream = io.StringIO()
    print(*args, file=stream, **kwargs)
    return stream.getvalue().strip()
