from math import floor
n = int(input())
times = []
max_speed = 0
for i in range(n):
    t, d = map(int, input().split())
    times.append((t, d))
for i in range(1, n):
    max_speed = max(max_speed, floor((times[i][1] - times[i - 1][1])/(times[i][0] - times[i - 1][0])))
print(max_speed)