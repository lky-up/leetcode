def bubbleSort(inputArray):
    for i in range(len(inputArray)):
        for j in range(len(inputArray)-1):
            if inputArray[j]>inputArray[j+1]:
                swapValue=inputArray[j]
                inputArray[j]=inputArray[j+1]
                inputArray[j+1]=swapValue
    return inputArray


