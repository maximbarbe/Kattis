from math import inf

def res(vals, target):
    start, end = 0, len(vals) - 1
    closest = inf
    r = None
    while start < end:
        cur = vals[start] + vals[end]
        if cur == target:
            return target
        else:
            if abs(target-cur) < closest:
                closest = abs(target - cur)
                r = cur
            if cur > target:
                end -= 1
            else:
                start += 1
    return r
case = 0
while True:
    case += 1
    try:
        n = int(input())
    except EOFError:
        break
    vals = []
    for i in range(n):
        vals.append(int(input()))
    vals.sort()
    m = int(input())
    print(f"Case {case}:")
    for i in range(m):
        t = int(input())
        print(f"Closest sum to {t} is {res(vals, t)}.")