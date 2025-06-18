n = int(input())
data = [*map(int, input().split(" "))]
copy = data.copy()
copy.sort()
res = 0
for i in range(len(data)):
    if data[i] != copy[i]:
        res += 1
print(res)