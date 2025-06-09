import itertools
from math import gcd
n = int(input())
vals = [*map(int, input().split(" "))]
for seq in itertools.permutations(vals):
    for i in range(len(seq) - 1):
        if gcd(seq[i], seq[i + 1]) == 1:
            break
    else:
        print(" ".join(map(str, seq)))
        exit()
else:
    print("Neibb")