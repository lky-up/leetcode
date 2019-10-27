def insertSort(inputArray):
    for i in range(len(inputArray)-1):
        current=inputArray[i+1]
        sign=i
        while(sign>=0 and current<inputArray[sign]):
            inputArray[sign+1]=inputArray[sign]
            sign-=1
        inputArray[sign+1]=current
    return inputArray

