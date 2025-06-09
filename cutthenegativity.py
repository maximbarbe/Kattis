n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split(" "))))
strings = []
res = 0    
for i in range(n):
    for j in range(n):
        if grid[i][j] != -1:
            res += 1
            strings.append(f"{i + 1} {j + 1} {grid[i][j]}")

print(res)
for string in strings:
    print(string)