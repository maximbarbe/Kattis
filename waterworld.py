n, m = map(int, input().split())
d = 360/m
slice = 1/m
res = 0
vals = []
for i in range(n):
    vals.append([*map(int, input().split())]) 
for i in range(n):
    for j in range(m):
        res += slice * (vals[i][j] * 1/n * 1/100)
print(res*100)