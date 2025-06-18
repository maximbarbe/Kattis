n = int(input())
res = 0
for i in range(1, n - 2):
    cur = i * (i + 1) * (i + 2)
    if cur >= n:
        break
    if cur < n:
        res += 1
print(res)