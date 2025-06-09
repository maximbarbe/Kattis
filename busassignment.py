n = int(input())
res = 0
cur = 0
for i in range(n):
    a, b = map(int, input().split())
    cur -= a
    cur += b
    res = max(res,cur)
print(res)