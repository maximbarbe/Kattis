from math import inf
n = int(input())
lower = -inf
upper = inf
for i in range(n):
    l,u = map(int,input().split())
    if l > upper or u < lower:
        print("bad news")
        exit()
    else:
        lower = max(lower, l)
        upper = min(upper, u)
print(upper-lower + 1, lower)