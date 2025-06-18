import sys

for line in sys.stdin:
    data = line.split(" ")
    month = data[0]
    day = data[1]
    year = data[2]
    first_time = [*map(int, data[3].split(":"))]
    second_time = [*map(int, data[4].split(":"))]
    if second_time[1] < first_time[1]:
        second_time[1] += 60
        second_time[0] -= 1
    diff = [second_time[0] - first_time[0], second_time[1] - first_time[1]]
    print(f"{month} {day} {year} {diff[0]} hours {diff[1]} minutes")