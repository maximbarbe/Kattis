n,m = map(int, input().split())
res = [0] * (n+m)
a = [*map(int, input().split())][::-1]
b = [*map(int, input().split())][::-1]
for i in range(len(a)):
    for j in range(len(b)):
        res[i + j] += a[i] * b[j]
while res and res[-1] == 0:
    res.pop()
if not res:
    res = [0]
print(*res[::-1])