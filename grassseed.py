cost = float(input())
n = int(input())
res = 0
for i in range(n):
    w, h = map(lambda x: float(x), input().split(" "))
    res += cost * w * h
print(res)