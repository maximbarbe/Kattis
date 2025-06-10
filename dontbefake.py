# Searching for overlapping intervals

seconds_in_the_day = [0 for i in range(24 * 60*60)]
n = int(input())
for i in range(n):
    data = [*map(int, input().split(" "))]
    m = data[0]
    data = data[1:]
    for j in range(len(data) // 2):
        for k in range(data[2*j], data[2*j + 1] + 1):
            seconds_in_the_day[k] += 1
num_seconds = 0
res = max(seconds_in_the_day)
print(res)
for j in range(24*60*60):
    if seconds_in_the_day[j] == res:
        num_seconds += 1
print(num_seconds)