a = int(input())

def lena(z):
    k = 0
    while z // 10 != 0:
        k += 1
        z = z // 10
    if z // 10 == 0:
        k += 1
    return (k == 1)


if lena(a) == True:
    print('Da!')
else:
    print('Net!')