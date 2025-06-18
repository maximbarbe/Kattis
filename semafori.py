n, l = map(int, input().split(" "))
cur_pos = 0
prev_time = 0
for i in range(n):
    dist, red, green = map(int, input().split(" "))
    prev_time += dist - cur_pos
    if prev_time % (red + green) < red:
        prev_time += red - (prev_time % (red + green))
    cur_pos = dist
prev_time += l - cur_pos
print(prev_time)