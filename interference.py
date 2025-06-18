n, w = map(int, input().split())
ranges = []
for i in range(n):
    data = input().split()
    if data[0] == "!":
        ranges.append((int(data[1]), int(data[1]) + int(data[2]), int(data[3])))
    else:
        res = 0
        pos = int(data[1])
        for l, h, a in ranges:
            if l <= pos < h:
                if (pos - l)% 4 == 0:
                    res += a
                elif (pos - l)%4 == 2:
                    res -= a
        print(res)