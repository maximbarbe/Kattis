remaining, m = map(int, input().split(" "))
vals = [*map(int, input().split(" "))]
missing = 0
for i in range(len(vals)):
    if remaining - vals[i] < 0:
        missing += 1
    else:
        remaining -= vals[i]
print(missing)