data = [*map(int, input().split(" "))]
size = data[0]
array = data[1:]
max_values = [0 for i in range(size)]
max_values[0] = array[0]

min_values = [0 for i in range(size)]
min_values[-1] = array[-1]

for i in range(1, size):
    max_values[i] = max(max_values[i - 1], array[i])
    
for i in range(size - 2, -1, -1):
    min_values[i] = min(min_values[i + 1], array[i])
    
res = []
for i in range(size):
    if max_values[i] <= array[i] and array[i] <= min_values[i]:
        res.append(array[i])
if len(res) == 0:
    print(0)
else:
    if len(res) > 100:
        print(len(res), end="")
        for i in range(100):
            print(f" {res[i]}")
    else:
        print(f"{len(res)} {' '.join(map(str, res))}")