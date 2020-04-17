a = int(input())
c = 0
arr = []


def lol(p):
    if p == 0:
        return
    else:
        lol(p // 2)
        c = p % 2
        arr.append(c)


lol(a)


def col_vo_null(x):
    k = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            k += 1
    print(k)


col_vo_null(a)
