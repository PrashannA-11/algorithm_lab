def Partition (A,start,end):
    pivot = A[end]
    pIndex = start
    for i in range(start,end):
        if(A[i] <= pivot):
            A[i],A[pIndex] = A[pIndex],A[i]
            pIndex += 1
    
    A[pIndex],A[end] = A[end],A[pIndex]
    
    return pIndex