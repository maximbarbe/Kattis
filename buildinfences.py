n = int(input())
minx = miny = 10**8 + 1
maxx = maxy = 0
for i in range(n):
    x, y = map(int, input().split())
    if x < minx:
        minx = x
    if x > maxx:
        maxx = x
    if y < miny:
        miny = y
    if y > maxy:
        maxy = y
    
print(2 * (maxx - minx + 2) + 2 * (maxy-miny + 2))