from itertools import permutations
from math import inf
n = input()
val = int(n)
smallest = inf
perms = permutations(n)
for perm in perms:
    joined = int("".join(perm))
    if  val < joined <smallest:
        smallest = joined
      
if smallest == inf:
    print(0)
else:
    print(smallest) 