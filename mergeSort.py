a = [int(x) for x in input().split()]


def mergeSort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    L = mergeSort(a[:mid])
    R = mergeSort(a[mid:])
    return merge(L, R)


def merge(A, B):
    C = []
    while A and B:
        if A[0] >= B[0]:
            C.append(A.pop(0))
        else:
            C.append(B.pop(0))
    return C + A + B


print(mergeSort(a))
