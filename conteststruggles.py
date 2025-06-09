n, k = map(int, input().split(" "))
d, s = map(int, input().split(" "))

res = (n *d - (k * s))/(n-k)
if res <0 or res > 100:
    print("impossible")
else:
    print(res)