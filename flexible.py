w, p = map(int, input().split(" "))
values = set()
distances =  [0] + [*map(int, input().split(" "))] + [w]
for i in range(len(distances) - 1):
    for j in range(i + 1, len(distances)):
        values.add(distances[j] - distances[i])
values = list(values)
values.sort()
print(" ".join(map(str, values)))