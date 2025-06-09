n = int(input())

values = [*map(int, input().split(" "))]
for i in range(len(values) -2, -1, -1):
    values[i] = min(values[i], values[i + 1])
print(sum(values))