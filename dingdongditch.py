n, q = map(int, input().split(" "))
data = [*map(int, input().split(" "))]
data.sort()
b = [*map(int, input().split(" "))]
sums = []
sums.append(data[0])
for i in range(1, len(data)):
    sums.append(sums[i - 1] + data[i])
for i in range(len(b)):
    print(sums[b[i] - 1])