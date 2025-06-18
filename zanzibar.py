n = int(input())
for i in range(n):
    data = list(map(int, input().split(" ")))
    res = 0
    for j in range(1, len(data)):
        if data[j] == 1 or data[j] <= 2 * data[j - 1]:
            continue
        else:
            res += data[j] - 2 * data[j - 1]
    print(res)