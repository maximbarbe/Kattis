n, a = map(int, input().split())
locks = set([*map(int, input().split())])
max_bi = max(locks)
powers = set()

cur = a
exp = 1
while cur <= max_bi:
    powers.add((cur, exp))
    cur *= a
    exp += 1
pairs = set()
for p, e in powers:
    for b in locks:
        if b%p == 0:
            pairs.add((e, b//p))
print(len(pairs))
