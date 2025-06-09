res = 0
n, m = map(int, input().split(" "))
vals = [*map(int, input().split(" "))]
for i in range(n - m + 1):
    count = 0
    for j in range(i, i+m):
        if vals[j] % 2 == 0:
            count += 1
        if count == 2:
            res += 1
            break
print(res)