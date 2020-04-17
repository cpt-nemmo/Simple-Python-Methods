a = int(input())


def IsPrime(N):
    if N % 2 == 0:
        return N == 2
    d = 3
    while d * d <= N and N % d != 0:
        d += 2
    return d * d > N


if IsPrime(a) == True:
    print('Число простое!')
else:
    print('Число составное!')
