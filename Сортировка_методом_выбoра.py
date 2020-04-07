arr = [int(x) for x in input().split()]


def vstavka_sort(mylist):
    k = 0
    n = len(arr)
    while k < n - 1:
        m = k
        i = k + 1
        while i < len(arr):
            if arr[i] < arr[m]:
                m = i
                print(mylist)
            i += 1
        arr[k], arr[m] = arr[m], arr[k]
        k += 1
    return mylist


print('Sorted list: ', vstavka_sort(arr))
