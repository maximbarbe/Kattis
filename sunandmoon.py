ds, ys = map(int, input().split(" "))
dm, ym = map(int, input().split(" "))
ds = -ds
dm = -dm
start = dm
cur = 0
while dm != ds:
    if ds < dm:
        ds += ys
    else:
        dm += ym
print(dm)