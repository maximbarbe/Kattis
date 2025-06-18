from math import floor,sqrt
string = input()
length = len(string)
rows = 0
cols = 0
for i in range(1, floor(sqrt(length)) + 1):
    if length % i == 0:
        rows = i
        cols = length // i
        
grid = [[None for i in range(cols)] for j in range(rows)]
res = ""
idx = 0
for i in range(cols):
    for j in range(rows):
        if idx != length:
            grid[j][i] = string[idx]
            idx += 1
    if idx == length:
        break
for i in range(rows):
    for j in range(cols):
        if grid[i][j] != None:
            res = "".join([res, grid[i][j]])
print(res)
