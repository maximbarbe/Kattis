n, m = map(int, input().split(" "))
x = 0
y = 0
seen = set()
num_moves = 0
grid = []
for i in range(n):
    grid.append(input())
while True:
    if (y, x) in seen:
        print("Lost")
        exit()
    if x < 0 or x == m or y < 0 or y == n:
        print("Out")
        exit()
    seen.add((y, x))
    if grid[y][x] == "T":
        print(num_moves)
        exit()
    elif grid[y][x] == "N":
        num_moves += 1
        y -= 1
    elif grid[y][x] == "S":
        num_moves += 1
        y += 1
    elif grid[y][x] == "E":
        num_moves += 1
        x += 1
    else:
        num_moves += 1
        x -= 1