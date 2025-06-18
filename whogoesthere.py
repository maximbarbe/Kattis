n, m = map(int, input().split())

schools = []
for i in range(m):
    schools.append(int(input()))
res = [0]*m
while n != 0:
    if min(schools) * m <= n and min(schools) != 0:
        k = min(schools)
        n -= k*m
        res = [*map(lambda el: el + k, res)]
        schools = [*map(lambda el: el - k, schools)]
    else:
        added = False
        for j in range(len(schools)):
            if schools[j] != 0 and n != 0:
                res[j] += 1
                schools[j] -= 1
                n -= 1
                added = True
        if not added:
            break
for r in res:
    print(r)