max_distance = 0

towers = input()
indices = []
for i in range(len(towers)):
    if towers[i] == "1":
        indices.append(i)
     
cur_tower_idx = 0
for i in range(len(indices) - 1):
    max_distance = max(max_distance, (indices[i + 1] - indices[i])//2)
print(max_distance)