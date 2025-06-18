num_judges, n = map(int, input().split(" "))
cur = 0
for i in range(n):
    cur += int(input())
min = cur
max = cur
for i in range(num_judges - n):
    min += -3
    max += 3
print(f"{round(min/num_judges, 4)} {round(max/num_judges, 4)}")