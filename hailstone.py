def h(n, cur):
    cur += n
    if n == 1:
        print(cur)
        exit()
    else:
        if n % 2 == 0:
            return h(n//2, cur)
        else:
            return h(3*n + 1, cur)
h(int(input()), 0)