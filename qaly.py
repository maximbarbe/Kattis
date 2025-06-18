n = int(input())
res = 0
for i in range(n):
    x, y = map(lambda x: float(x), input().split(" "))
    res += x * y
print(round(res, 3))