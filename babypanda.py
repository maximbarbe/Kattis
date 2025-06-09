from math import log2, floor

n, m = map(int, input().split(" "))
res = 0
if m == 0:
    print(0)
    exit()
while True:
    if log2(m) == int(log2(m)):
        res += 1
        break
    else:
        m -= 2**floor(log2(m))
        res += 1
print(res)