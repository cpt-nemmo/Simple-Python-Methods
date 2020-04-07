arr = [int(x) for x in input().split()]


def insert_sort(array):
    for i in range(1, len(array)):
        key = arr[i]
        j = i - 1
        while (j >= 0) and (key < array[j]):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        print(array)
    return array


print('Sorted array: ', insert_sort(arr))
