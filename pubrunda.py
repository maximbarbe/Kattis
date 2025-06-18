n = int(input())
max_time = 0
res = None
for i in range(n):
    name, k, t = input().split()
    k = int(k)
    t = int(t)
    if (k + 1)*t > max_time:
        max_time = (k + 1) * t
        res = name
print(res, max_time)