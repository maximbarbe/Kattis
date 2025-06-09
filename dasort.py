n = int(input())
for i in range(n):
    k, el = map(int, input().split())
    vals = []
    while len(vals) != el:
        vals.extend([*map(int, input().split())])
    temp = sorted(vals.copy())

    sidx = 0
    idx = 0
    while idx != len(vals):
        if vals[idx] == temp[sidx]:
            sidx += 1
        idx += 1
    print(k, len(vals) - sidx)