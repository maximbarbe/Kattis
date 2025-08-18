apps = []
seen = set()
res = []
for i in range(int(input())):
    n, *a = input().split()
    apps.append(a)
for v in apps:
    for k in v:
        if k not in seen:
            res.append(k)
            seen.add(k)
            break
print(*res)