n = int(input())
data = list(map(int, input().split(" ")))
cur = 0
for item in data:
    if item == -1:
        n -= 1
    else:
        cur += item
print(round(cur/n, 3))