n, p, q = map(int, input().split(" "))

if (p + q)% (2*n) >= n:
    print("opponent")
else:
    print("paul")