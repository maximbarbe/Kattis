n = int(input())
vals = [*map(int, input().split())]
vals.sort()
print(vals[0] + vals[1])