n, m = map(int, input().split(" "))
sets = []
for i in range(n):
    sets.append(set(input().split(" ")))
cur = sets[0]
for i in range(1, len(sets)):
    cur = cur.intersection(sets[i])
print(len(cur))
cur = sorted(cur)
for el in cur:
    print(el)