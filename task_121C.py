d = 0


def roling(x):
    if x == 0:
        return
    else:
        roling(x // 16)
        d = x % 16
        if d <= 9:
            print(d, end='')
        elif d == 10:
            print('A')
        elif d == 11:
            print('B')
        elif d == 12:
            print('C')
        elif d == 13:
            print('D')
        elif d == 14:
            print('E')
        elif d == 15:
            print('F')


c = int(input())
roling(c)
