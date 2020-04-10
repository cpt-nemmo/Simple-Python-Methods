a = int(input())


def triangle(n):
    print('0')
    k = 1
    for i in range(n - 1):
        print('0' + '0' * k)
        k += 1


triangle(a)