from collections import deque
while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    diameters = []
    heights = []
    for i in range(n):
        diameters.append(int(input()))
    for i in range(m):
        heights.append(int(input()))
    if m < n:
        print("Loowater is doomed!")
        continue
    heights.sort()
    diameters.sort()
    d = deque(diameters)
    h = deque(heights)
    res = 0
    while d and h:
        while h and h[0] < d[0]:
            h.popleft()
        if not h:
            break
        res += h.popleft()
        d.popleft()
    if len(d) != 0:
        print("Loowater is doomed!")
    else:
        print(res)