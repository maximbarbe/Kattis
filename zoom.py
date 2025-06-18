n, k = map(int, input().split(" "))

res = []
data = list(map(int, input().split(" ")))
for i in range(len(data)):
    if (i + 1) % k == 0:
        res.append(str(data[i]))
print(" ".join(res))