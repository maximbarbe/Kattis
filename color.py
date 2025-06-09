num_socks, capacity, max_diff = map(int, input().split(" "))


values = [*map(int, input().split(" "))]
values.sort()
res = 0
min_value = None
current_washer = 0
for i in range(len(values)):
    if min_value == None:
        min_value = values[i]
        res += 1
        current_washer = 1
    elif current_washer == capacity:
        min_value = values[i]
        res += 1
        current_washer = 1
    elif abs(values[i] - min_value) > max_diff:
        min_value = values[i]
        res += 1
        current_washer = 1
    else:
        current_washer += 1
print(res)