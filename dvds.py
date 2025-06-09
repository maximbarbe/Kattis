from bisect import bisect_left



t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    cur = 1
    for val in vals:
        if val == cur:
            cur += 1
    print(n - cur + 1)