from math import inf

pa, ka, pb, kb, n = map(int, input().split())

min_cost = inf
numA = 0
numB = 0
for i in range(n+1):

    b = (n - i)
    if i % ka == 0:
        numa = (i // ka)
        costA = (i // ka) * pa
    else:
        numa = (i // ka + 1)
        costA = (i // ka + 1) * pa
    if b % kb == 0:
        numb = (b // kb)
        costB = (b // kb) * pb
    else:
        numb = (b // kb + 1)
        costB = (b // kb + 1) * pb
    if costA + costB < min_cost:
        min_cost = costA + costB
        numA = numa
        numB = numb
        
print(numA, numB, min_cost)