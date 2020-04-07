arr1 = [int(x) for x in input().split()]


def bubble_sort(mylist):
    last_index = len(mylist) - 1
    for i in range(0, last_index):
        for x in range(0, last_index - i):
            print(mylist)
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]
    return mylist


print('arr1: ', arr1)
newlist = bubble_sort(arr1).copy()
print('New List :', newlist)
