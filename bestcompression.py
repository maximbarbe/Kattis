from math import ceil, log2

n, b = map(int, input().split(" "))
if 2**(b + 1) -1>= n:
    print("yes")
else:
    print("no")