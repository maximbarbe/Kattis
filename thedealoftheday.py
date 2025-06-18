import itertools

vals = [*map(int, input().split(" "))]
k = int(input())
nonzeroes = []
for i in range(len(vals)):
    if vals[i] != 0:
        nonzeroes.append(i)

res = 0
for comb in itertools.combinations(nonzeroes, k):
    prod = 1
    for el in comb:
        prod *= vals[el]
    res += prod
print(res)