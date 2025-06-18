t=  int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    res = 0
    vals.sort()
    first, sec = 0, len(vals) -2
    while first < sec:
        res += vals[sec]
        first += 1
        sec -= 2
    print(res)