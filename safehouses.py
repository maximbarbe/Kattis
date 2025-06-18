from math import inf
spies = []
houses = []
distances = []


n = int(input())
for i in range(n):
    row = input()
    for j in range(len(row)):
        if row[j] == "H":
            houses.append((i, j))
        elif row[j] == "S":
            spies.append((i, j))
            
for spy in spies:
    cur_min = inf
    for house in houses:
        dist = abs(house[0] - spy[0]) + abs(house[1] - spy[1])
        if dist < cur_min:
            cur_min = dist
    distances.append(cur_min)
print(max(distances))