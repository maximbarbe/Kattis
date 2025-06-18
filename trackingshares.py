from bisect import bisect_left


companies = []
days = set()
c = int(input())
for i in range(c):
    k = int(input())
    shares = []
    for j in range(k):
        n, d = map(int, input().split())
        shares.append((n, d))
        days.add(d)
    shares.sort(key=lambda el:el[1])
    companies.append(shares)
res = []
for d in sorted(days):
    cur = 0
    for c in companies:
        m = 0
        for n, d1 in c:
            if d1 <= d:
                m = n
            else:
                break
        cur += m
    res.append(cur)
print(*res)