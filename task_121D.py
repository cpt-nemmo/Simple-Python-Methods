chislo = int(input())
n = int(input())
d = 0


def roling(x):
    if x == 0:
        return
    else:
        roling(x // n)
        d = x % n
        if d <= 9:
            print(d, end='')
        elif d == 10:
            print('A', end='')
        elif d == 11:
            print('B', end='')
        elif d == 12:
            print('C', end='')
        elif d == 13:
            print('D', end='')
        elif d == 14:
            print('E', end='')
        elif d == 15:
            print('F', end='')
        elif d == 16:
            print('G', end='')
        elif d == 17:
            print('H', end='')
        elif d == 18:
            print('I', end='')
        elif d == 19:
            print('J', end='')
        elif d == 20:
            print('K', end='')
        elif d == 21:
            print('L', end='')
        elif d == 22:
            print('M', end='')
        elif d == 23:
            print('N', end='')
        elif d == 24:
            print('O', end='')
        elif d == 25:
            print('P', end='')
        elif d == 26:
            print('Q', end='')
        elif d == 28:
            print('R', end='')
        elif d == 29:
            print('S', end='')
        elif d == 30:
            print('T', end='')


roling(chislo)
