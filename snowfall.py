res = 0
n = int(input())
for i in range(n):
    t, a = map(int, input().split())
    if t == 0:
        res += a
    else:
        res = max(0, res-a)
print(res)