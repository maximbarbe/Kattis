n, t, a, b = map(int, input().split())

increasing = True
increasing_res = 0
stops = [*map(int, input().split())]
prev = a
for i in range(t):
    if increasing:
        if stops[i] >= prev:
            prev = stops[i]
        else:
            increasing = False
            increasing_res += 1
            prev = stops[i] + 1
    else:
        if stops[i] < prev:
            prev = stops[i] + 1
        else:
            increasing = True
            increasing_res += 1
            prev = stops[i]

if increasing:
    if b <= prev:
        increasing_res += 1
else:
    if b >= prev:
        increasing_res += 1


decreasing_res = 0
increasing = False
prev = a
for i in range(t):
    if increasing:
        if stops[i] >= prev:
            prev = stops[i]
        else:
            increasing = False
            decreasing_res += 1
            prev = stops[i] + 1
    else:
        if stops[i] < prev:
            prev = stops[i] + 1
        else:
            increasing = True
            decreasing_res += 1
            prev = stops[i]

if increasing:
    if b <= prev:
        decreasing_res += 1
else:
    if b >= prev:
        decreasing_res += 1
        
print(min(increasing_res, decreasing_res))