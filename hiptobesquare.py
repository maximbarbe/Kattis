t = int(input())
for i in range(t):
    max_size = 0
    n = int(input())
    for j in range(1, 10**5 + 2, 2):
        if j**2 -1 <= n:
            max_size = j
        else:
            break
    if max_size == 0:
        print(0)
    else:
        print((max_size - 1)//2)