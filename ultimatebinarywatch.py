time = input()
grid = [[],
        [],
        [],
        []]
for char in time:
    binary = bin(int(char))[2:]
    binary = "0" * (4 - len(binary)) + binary
    for i in range(len(binary)):
        if binary[i] == '0':
            grid[i].append(".")
        else:
            grid[i].append("*")
for row in grid:
    row.insert(2, ' ')
    
for row in grid:
    print(' '.join(row))