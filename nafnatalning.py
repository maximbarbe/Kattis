n, p = map(int, input().split())
vals = [*map(int, input().split())]
to_see = sum(vals)
pairs_to_see = []
res = 0
for i in range(len(vals)):
    pairs_to_see.append(to_see - vals[i])
considered_pairs = 0
for i in range(len(pairs_to_see)):
    pairs_to_see[i] -= considered_pairs
    res += pairs_to_see[i] * vals[i]
    considered_pairs += vals[i]
    
    
if res % p == 0:
    print(res//p)
else:
    print(res//p + 1)