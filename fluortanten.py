from math import inf

n = input()
values = [*map(int, input().split(" "))]
array = [0] + [values[i] for i in range(len(values)) if values[i] != 0]
left = 0
right = 0
max_value = -inf
for i in range(1, len(array)):
    right += array[i] * (i + 1)
if left + right > max_value:
    max_value = left + right
for i in range(len(array) - 1):
    right -= array[i + 1] * (i + 2)
    left += array[i + 1] * (i + 1)
    array[i], array[i + 1] = array[i + 1], array[i]
    if left + right > max_value:
        max_value = left + right
print(max_value)