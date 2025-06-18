n, m = map(int, input().split())

grid = []
for i in range(n):
    grid.append(input())
spots_left = False
handshakes = 0
for i in range(n):
    for j in range(m):
        
        if grid[i][j] == "o":
            one_more_row = False
            one_more_col = False
            if i + 1 < n:
                one_more_row = True
                if grid[i + 1][j] == "o":
                    handshakes += 1
            if j + 1 < m:
                one_more_col = True
                if grid[i][j+1] == "o":
                    handshakes += 1
                
            if one_more_row and j - 1 >= 0:
                if grid[i+1][j-1] == "o":
                    handshakes += 1
            if one_more_row and one_more_col: 
                if grid[i+1][j+1] == "o":
                    handshakes += 1

add = 0
for i in range(n):
    for j in range(m):
        cur = 0
        if grid[i][j] == ".":
            for x, y in [(0, 1), (0, -1), (1, 1), (1, -1), (-1,0), (-1, 1), (-1, -1), (1, 0)]:
                if i + x >= 0 and i + x < n and j + y >= 0 and j + y < m and grid[i+x][j+y] == "o":
                    cur += 1
        if cur > add:
            add = cur
            
print(handshakes + add)