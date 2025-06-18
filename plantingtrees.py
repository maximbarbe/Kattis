n = int(input())
data = [*map(int, input().split(" "))]
data.sort(reverse=True)
for i in range(len(data)):
    data[i] += i + 1
print(max(data) + 1)