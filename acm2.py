n, idx = map(int, input().split(" "))
vals = [*map(int, input().split(" "))]
total = 0
penalty = 0
time = 0
if vals[idx] > 300:
    print("0 0")
    exit()
else:
    temp = vals.pop(idx)
    total += 1
    time += temp
    penalty += time
    vals.sort()
    for i in range(len(vals)):
        if time + vals[i] <= 300:
            total += 1
            time += vals[i]
            penalty += time
            
    print(f"{total} {penalty}")