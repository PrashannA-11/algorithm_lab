def merge(L, R, A):
    i = j = k = 0

    # Merge elements from L and R into A
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # Append remaining elements from L (if any)
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    # Append remaining elements from R (if any)
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

    return A