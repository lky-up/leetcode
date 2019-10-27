def selectSort(inputArray):
    for i in range(len(inputArray)):
        minIndex=i
        for j in range(i+1,len(inputArray)):
            if inputArray[j]<inputArray[minIndex]:
                minIndex=j
        swapValue=inputArray[i]
        inputArray[i]=inputArray[minIndex]
        inputArray[minIndex]=swapValue
    return inputArray
