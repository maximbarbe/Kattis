n,s,r = map(int, input().split(" "))

damaged = set([*map(int, input().split(" "))])
reserved = set([*map(int, input().split(" "))])
res = 0
for i in range(1, n+1):
    if i in damaged:
        if i - 1 in reserved:
            reserved.remove(i - 1)
        elif i + 1 in reserved:
            reserved.remove(i + 1)
        else:
            res += 1
print(res)