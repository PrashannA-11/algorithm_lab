from partition import Partition


def quicksort(A,start,end):
    if (start < end):
        pIndex = Partition(A,start,end)
        quicksort(A,start,pIndex-1)
        quicksort(A,pIndex+1,end)
    
    return A

