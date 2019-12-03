def popSeveral(inputList, count):
    data = inputList[-count:]
    inputList = inputList[:-count]
    return (inputList, data)
