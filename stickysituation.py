n = int(input())
vals = [*map(int, input().split())]
vals.sort()
for i in range(len(vals) - 2):
    if vals[i] + vals[i + 1] > vals[i + 2]:
        print("possible")
        exit()
else:
    print("impossible")