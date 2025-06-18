string = input()
grid = [["." for i in range(5 + 4 * (len(string) - 1))] for j in range(5)]

for i in range(len(string)):
    letter_pos = 2 + i * 4
    grid[2][letter_pos] = string[i]
    if i % 3 == 2:
        grid[0][letter_pos] = "*"
        grid[4][letter_pos] = "*"
        grid[1][letter_pos - 1] = "*"
        grid[1][letter_pos  + 1] = "*"
        grid[2][letter_pos - 2] = "*"
        grid[2][letter_pos + 2] = "*"
        grid[3][letter_pos - 1] = "*"
        grid[3][letter_pos + 1] = "*"
    else:
        if i == 0:
            grid[2][letter_pos - 2] = "#"
        grid[0][letter_pos] = "#"
        grid[4][letter_pos] = "#"
        grid[1][letter_pos - 1] = "#"
        grid[1][letter_pos  + 1] = "#"
        grid[2][letter_pos + 2] = "#"
        grid[3][letter_pos - 1] = "#"
        grid[3][letter_pos + 1] = "#" 
for row in grid:
    print("".join(row))