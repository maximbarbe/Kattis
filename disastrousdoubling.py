n = int(input())
vals = [*map(int, input().split())]
cur = 1
for v in vals:
    cur *= 2
    if v > cur:
        print("error")
        exit()
    else:
        cur -= v
else:
    print(cur % (10**9 + 7))