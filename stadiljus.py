n = int(input())
cost = int(input())
max_average = int(input())
vals = [*map(int, input().split())]
vals.sort()
num = 0
denom = 0
res = 0
for i in range(len(vals)):
    if (num + cost*vals[i])/(denom + 1) <= max_average:
        res += 1
        num += cost*vals[i]
        denom += 1
    else:
        break
    
print(res)