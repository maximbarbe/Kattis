s, n, m = map(int, input().split(" "))
values = []
while len(values) != s:
    
    values += [*map(int, input().split(" "))]
increasing_left = [0 for i in range(s)]
increasing_right = [0 for i in range(s)]
decreasing_left = [0 for i in range(s)]
decreasing_right = [0 for i in range(s)]
decreasing_left[0] = 1
decreasing_right[-1] = 1
increasing_right[-1] = 1
increasing_left[0] = 1
for i in range(1, s):
    if values[i] > values[i - 1]:
        increasing_left[i] = 1 + increasing_left[i - 1]
        decreasing_left[i] = 1
    else:
        increasing_left[i] = 1
        decreasing_left[i] = 1 + decreasing_left[i - 1]
for i in range(s - 2, -1, -1):
    if values[i] > values[i + 1]:
        increasing_right[i] = 1 + increasing_right[i + 1]
        decreasing_right[i] = 1
    else:
        increasing_right[i] = 1
        decreasing_right[i] = decreasing_right[i + 1] + 1
peaks = 0
valleys = 0
for i in range(s):
    if increasing_left[i] >= n and increasing_right[i] >= n:
        peaks += 1
    if decreasing_left[i] >= m and decreasing_right[i] >= m:
        valleys += 1
print(f"{peaks} {valleys}")