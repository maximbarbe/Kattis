from math import inf

n = int(input())
closest = inf
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 * x2 < 0:
        m = (y2 -y1)/(x2-x1)
        b = y1 - m*x1
        if b < 0:
            continue
        else:
            closest = min(closest, b)
    else:
        continue
    
    
if closest == inf:
    print("-1.0")
else:
    print(closest)