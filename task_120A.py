def diamond_glisen(x):
    if x == 0:
        return
    else:
        diamond_glisen(x // 8)
        print(x % 8, end='')


b=int(input())
diamond_glisen(b)
