a = int(input())


def chpok_v_pupok(x):
    return (x % 10 == 0)


if chpok_v_pupok(a) == True:
    print('Da!')
else:
    print('Net!')

