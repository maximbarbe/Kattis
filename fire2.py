from collections import deque
t = int(input())
while t != 0:
    col, row = map(int, input().split())
    next_iter_fire = deque()
    next_iter_person = deque()
    grid = []
    for i in range(row):
        r = [*input()]
        for j in range(col):
            if r[j] == "@":
                next_iter_person.append((i, j))
            elif r[j] == "*":
                next_iter_fire.append((i, j))    
        grid.append(r)
    second = 0
    found_exit = False
    while len(next_iter_person) != 0:
        cur_iter_person = next_iter_person
        cur_iter_fire = next_iter_fire
        next_iter_person = deque()
        next_iter_fire = deque()
        for i, j in cur_iter_person:
            if grid[i][j] == "@":
                for x, y in [(0, 1), (0, - 1), (1, 0), (-1, 0)]:
                    if i + x >= 0 and i + x < row and j + y >= 0 and j + y < col:
                        if grid[i+x][j+y] == ".":
                            grid[i+x][j+y] = "@"
                            next_iter_person.append((i + x, y +j))
                    else:
                        print(second + 1)
                        found_exit = True
                        break
            if found_exit:break
        
        if found_exit:
            break
        for i, j in cur_iter_fire:
            for x, y in [(0, 1), (0, - 1), (1, 0), (-1, 0)]:
                if i + x >= 0 and i + x < row and j + y >= 0 and j + y < col:
                    if grid[i+x][j+y] in ".@":
                        grid[i+x][j+y] = "*"
                        next_iter_fire.append((i+x, j+y))
        second += 1
    else:
        print("IMPOSSIBLE")
    
    
    
    
    
    
    
    
    
    
    
    
    
    t -= 1