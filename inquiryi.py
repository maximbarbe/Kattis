n = int(input())

res = 0
vals = []
for i in range(n):
    vals.append(int(input()))
    
ssq = 0
sumn = sum(vals)
for i in range(len(vals)):
    ssq += vals[i] ** 2
    sumn -= vals[i]
    if ssq * sumn > res:
        res = ssq * sumn
        
print(res)