def shellSort(inputArray):
    gap=int(len(inputArray)/2)
    while gap>=1:
        for i in range(gap,len(inputArray)):
            swapValue=inputArray[i]
            preIndex=i-gap
            while(preIndex>=0 and inputArray[preIndex]>swapValue):
                inputArray[preIndex+gap]=inputArray[preIndex]
                preIndex-=gap
            inputArray[preIndex+gap]=swapValue
        gap=int(gap/2)
    return inputArray





