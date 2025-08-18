t = int(input())
vals = [*map(int, input().split())]
res = 0 
prev = 0
for v in vals:
    res += abs(v - prev)
    prev = v
print(res)