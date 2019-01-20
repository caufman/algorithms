def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                tmp = array[j+1]
                array[j+1] = array[j]
                array[j] = tmp
    return array
    
def selectionSort(array):
    def minFind(subarray):
        if len(subarray) > 1:
            subMin = minFind(subarray[1:])
            return subarray[0] if subarray[0] < subMin else subMin
        else:
            return subarray[0]
            
    for i in range(len(array)):
        ind = array[i:].index(minFind(array[i:]))+i
        tmp = array[i]
        array[i] = array[ind]
        array[ind] = tmp
    return array
    
def insertionSort(array):
    for i in range(1, len(array)):
        for j in range(i):
            while array[i] < array[j]:
                tmp = array[i]
                array[i] = 
