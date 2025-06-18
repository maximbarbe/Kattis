s, n = map(int, input().split())
vals = [*map(int, input().split())]
seated = [False for i in range(s)]
for val in vals:
    seated[val - 1] = True
    
i = vals[0]
res = 0
while i != vals[0] - 1:
    if seated[(i - 1)%s] == False and seated[(i + 1) % s] == False and seated[i] == False:
        res += 1
        seated[i] = True
    i = (i + 1)%s
print(res)