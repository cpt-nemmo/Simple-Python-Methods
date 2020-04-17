a = int(input())


def number(x):
    k = 0
    while x // 10 != 0:
        k += 1
        x = x // 10
    if x // 10 == 0:
        k += 1
    print(k)


number(a)
