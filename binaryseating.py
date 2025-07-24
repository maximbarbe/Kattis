n = int(input())
vals = [*map(int, input().split())]
vals.sort(reverse=True)
res = 0
t = 2**n
p = 1
for i in range(len(vals)):
    p /= 2
    res += vals[i] * p
    
print(res)