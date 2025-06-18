n = int(input())
for i in range(n):
    data = [*map(int, input().split())]
    k = data[0]
    vals = data[1:]
    res = 0
    for i in range(1, len(vals) - 1):
        if vals[i - 1]>= vals[i]:
            continue
        for j in range(len(vals) -1, i, - 1):
            if vals[j] < min(vals[i:j]) and min(vals[i:j])>vals[i - 1]:
                res += 1
    print(k, res)