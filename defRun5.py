a = int(input())


def square(n):
    print('0' * n)
    for i in range(n - 2):
        print('0' + ' ' * (n-2) + '0')
    print('0' * n)


square(a)
