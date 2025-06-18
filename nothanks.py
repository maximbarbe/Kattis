n = int(input())
res = 0
vals = [*map(int, input().split(" "))]
vals.sort()
i = 0
while i != len(vals):
    prev = vals[i]
    j = i + 1
    while j != len(vals) and vals[j] - prev == 1:
        prev = vals[j]
        j += 1
        
    res += vals[i]
    i = j
print(res)