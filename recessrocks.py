n = int(input())
vals = sorted([*map(int, input().split())])
res = 0
for i in range(1, n):
    if vals[i] == vals[i - 1]:
        res += 1
print(res)