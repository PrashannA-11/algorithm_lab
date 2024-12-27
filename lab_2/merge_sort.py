from merge import merge

def mergesort(A):
    if len(A) < 2:
        return

    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]

    mergesort(left)
    mergesort(right)
    merge(left, right, A)

    return A