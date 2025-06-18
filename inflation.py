n = int(input())
vals = [*map(int, input().split(" "))]
max_fraction = 1
vals.sort()
for i in range(n):
    if vals[i] > i + 1:
        print("impossible")
        exit()
    else:
        frac = vals[i]/(i + 1)
        if frac < max_fraction:
            max_fraction = frac
            
print(max_fraction)