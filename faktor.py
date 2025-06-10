import math
n, m = map(lambda x: int(x), input().split(" "))
i = n * m
while i != 0 and math.ceil(i / n) == m:
    i -= 1
print(i + 1)