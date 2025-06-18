from math import inf
n = int(input())
temps = [*map(int, input().split(" "))]

max_temp = inf
start = 0
for i in range(len(temps) - 2):
    if max(temps[i], temps[i + 2]) < max_temp:
        max_temp = max(temps[i], temps[i + 2])
        start = i
        
print(f"{start  + 1} {max_temp}")