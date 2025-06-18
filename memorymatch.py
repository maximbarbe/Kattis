from collections import defaultdict

n = int(input())


pairs_seen = dict()
indices = defaultdict(lambda:set())
t = int(input())
for i in range(t):
    idx1, idx2, type1, type2 = input().split()
    idx1 = int(idx1)
    idx2 = int(idx2)
    indices[type1].add(idx1)
    indices[type2].add(idx2)
    if type1==type2:
        pairs_seen[type1] = True
        
res = 0

for key, val in indices.items():
    if len(val) == 2:
        if pairs_seen.get(key, False) == False:
            res += 1
if len(indices.keys()) == n//2 - 1:
    for val in indices.values():
        if len(val) != 2:
            print(res)
            exit()
    else:
        print(res + 1)
elif len(indices.keys()) != n//2:
    print(res)
else:
    for key, val in indices.items():
        if len(val) == 1:
            res += 1
    print(res)