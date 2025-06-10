import itertools 
from collections import defaultdict

n = int(input())

for i in range(n):
    sums = defaultdict(lambda:None)
    data = [*map(int, input().split(" "))]
    vals = data[1:]
    printed = False
    for j in range(1, 21):
        combs = itertools.combinations(vals, j)
        for el in combs:
            if sums[sum(el)] != None:
                print(f"Case #{i+1}:")
                print(" ".join(map(str, el)))
                print(" ".join(map(str, sums[sum(el)])))
                printed = True
                break
            else:
                sums[sum(el)] = el
        if printed:
            break