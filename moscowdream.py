e, m, d, n = map(int, input().split(" "))
if e == 0 or m == 0 or d == 0 or n < 3:
    print("NO")
    exit()
e -= 1
m -= 1
d -= 1
if e + m + d < n - 3:
    print("NO")
    exit()
else:
    print("YES")