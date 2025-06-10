n = int(input())
m = int(input())

sheep = 0
if m > 4*n or m%2 == 1:
    print("Rong talning")
else:
    while 4 * n != m:
        m -= 2
        n -= 1
        if n < 0:
            break
    if n < 0:
        print("Rong talning")
    else:
        print(n)