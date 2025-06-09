n = int(input())
for i in range(n):
    m = int(input())
    indices = [i for i in range(m)]
    res = [0 for i in range(m)]
    for k in range(1, m + 1):
        for l in range(k):
            indices.append(indices.pop(0))
        res[indices[0]] = k
        indices.pop(0)
    print(" ".join(map(str, res)))