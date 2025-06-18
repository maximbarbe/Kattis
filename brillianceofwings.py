n = int(input())
original = set()
for i in range(n-1):
    u, v = map(int, input().split())
    original.add((min(u, v), max(u, v)))
res = 0
for i in range(n-1):
    u, v = map(int, input().split())
    if (min(u, v), max(u, v)) not in original:
        res += 1
print(res)