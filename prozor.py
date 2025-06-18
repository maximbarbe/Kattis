R, S, racket = map(int, input().split(" "))
grid = []
min_flies = 0
top_left = (0, 0)
bot_right = (0, 0)
for i in range(R):
    grid.append(input())
for i in range(R - racket  + 1):
    for j in range(S- racket + 1):
        flies = 0
        for k in range(i + 1, i + racket - 1):
            for l in range(j + 1, j + racket - 1):
                if grid[k][l] == "*":
                    flies += 1
        if flies>min_flies:
            min_flies = flies
            top_left = (i, j)
            bot_right = (i + racket - 1, j + racket - 1)
print(min_flies)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (i, j) == top_left or (i, j) == bot_right or (i, j) == (top_left[0], bot_right[1]) or (i,j) == (bot_right[0], top_left[1]):
            print("+", end="")
        elif i == top_left[0] and top_left[1] < j < bot_right[1]:
            print("-", end="")
        elif i == bot_right[0] and top_left[1] < j < bot_right[1]:
            print("-", end="")
        elif j == top_left[1] and top_left[0] < i < bot_right[0]:
            print("|", end="")
        elif j == bot_right[1] and top_left[0]<i<bot_right[0]:
            print("|", end="")
        else:
            print(grid[i][j], end="")
    print()