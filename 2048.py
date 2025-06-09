def move_left(grid):
    idx = 0
    for row in grid:
        
        compressed_row = []
        for i in range(4):
            if row[i] != 0:
                compressed_row.append(row[i])
        combined = []
        i = 0
        while len(compressed_row) > 1:
            if compressed_row[i] == compressed_row[i + 1]:
                combined.append(compressed_row[i] * 2)
                compressed_row.pop(i)
                compressed_row.pop(i)
            else:
                combined.append(compressed_row[i])
                compressed_row.pop(i)
                
        if compressed_row != []:
            combined.append(compressed_row[0])
        combined += [0 for i in range(4 - len(combined))]
        grid[idx] = combined
        idx += 1
    for i in range(len(grid)):
        print(" ".join(map(lambda x: str(x), grid[i])))

def move_right(grid):
    idx = 0
    for row in grid:
        
        compressed_row = []
        for i in range(4):
            if row[i] != 0:
                compressed_row.append(row[i])
        combined = []
        
        while len(compressed_row) > 1:
            i = len(compressed_row) - 1
            if compressed_row[i] == compressed_row[i - 1]:
                combined.insert(0, compressed_row[i] * 2)
                compressed_row.pop(i)
                compressed_row.pop(i - 1)
            else:
                combined.insert(0, compressed_row[i])
                compressed_row.pop(i)
                
        if compressed_row != []:
            combined.insert(0, compressed_row[0])
        combined = [0 for i in range(4 - len(combined))] + combined
        grid[idx] = combined
        idx += 1
    for i in range(len(grid)):
        print(" ".join(map(lambda x: str(x), grid[i])))    
def move_up(grid):
    
    for j in range(4):
        compressed_col = []
        for i in range(4):
            if grid[i][j] != 0:
                compressed_col.append(grid[i][j])
        combined = []
        i = 0
        while i < len(compressed_col) - 1:
            if compressed_col[i] == compressed_col[i + 1]:
                combined.append(compressed_col[i] * 2)
                compressed_col.pop(i)
                compressed_col.pop(i)
            else:
                combined.append(compressed_col[i])
                compressed_col.pop(i)
        if compressed_col != []:
            combined.append(compressed_col[-1])
        combined += [0 for i in range(4 - len(combined))]
        for i in range(4):
            grid[i][j] = combined[i]            
    for i in range(len(grid)):
        print(" ".join(map(lambda x: str(x), grid[i])))   


def move_down(grid):
    
    for j in range(4):
        compressed_col = []
        for i in range(4):
            if grid[i][j] != 0:
                compressed_col.append(grid[i][j])
        combined = []
        i = 0
        while len(compressed_col) > 1:
            i = len(compressed_col) - 1
            if compressed_col[i] == compressed_col[i - 1]:
                combined.insert(0, compressed_col[i] * 2)
                compressed_col.pop(i)
                compressed_col.pop(i - 1)
            else:
                combined.insert(0, compressed_col[i])
                compressed_col.pop(i)
                
        if compressed_col != []:
            combined.insert(0, compressed_col[0])
        combined = [0 for i in range(4 - len(combined))] + combined
        for i in range(4):
            grid[i][j] = combined[i]            
    for i in range(len(grid)):
        print(" ".join(map(lambda x: str(x), grid[i])))    


grid = [[0 for i in range(4)] for j in range(4)]
for i in range(4):
    grid[i] = list(map(lambda x:int(x), input().split(" ")))
move = int(input())
if move == 0:
    move_left(grid)
elif move == 1:
    move_up(grid)
elif move == 2:
    move_right(grid)
else:
    move_down(grid)  
