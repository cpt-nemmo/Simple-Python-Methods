chislo = int(input())
n = int(input())


def yosemite(x):
    if x == 0:
        return
    else:
        yosemite(x // n)
        print(x % n, end='')


yosemite(chislo)
