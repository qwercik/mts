def popSeveral(inputList, count):
    data = inputList[-count:]
    for i in range(count):
        inputList.pop()

    return data 
