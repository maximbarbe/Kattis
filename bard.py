n = int(input())
k = int(input())
cur = set([1])
for i in range(k):
    e, *v = [*map(int, input().split())]
    v = set(v)
    if 1 in v:
        cur = cur.intersection(v)
    else:
        cur = cur.union(v)
for val in sorted(cur):
    print(val)