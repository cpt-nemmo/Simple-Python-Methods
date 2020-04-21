import random
a = [int(x) for x in input().split()]


def qSort(a):
    if len(a) <= 1:
        return a
    x = random.choice(a)
    BL = [b for b in a if b < x]
    BX = [b for b in a if b == x]
    BR = [b for b in a if b > x]
    return qSort(BR) + BX + qSort(BL)


print(qSort(a))
