def solve(a, b, n, m):
    grid = [[None for i in range(a)] for j in range(b)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    positions = dict()
    for i in range(n):
        x,y, letter = input().split()
        match letter:
            case "N":
                idx = 3
            case "E":
                idx = 0
            case "S":
                idx = 1
            case "W":
                idx = 2
        grid[b-int(y)][int(x) - 1] = (i + 1, idx)
        positions[i + 1] = (b-int(y), int(x) - 1)
    string = ""
    for i in range(m):

        robot, action, repeat = input().split()
        if string:
            continue
        cury, curx = positions[int(robot)]
        r = int(repeat)
        match action:
            
            case "L":
                grid[cury][curx] = (grid[cury][curx][0], (grid[cury][curx][1] - r)%4)
            case "R":
                grid[cury][curx] = (grid[cury][curx][0], (grid[cury][curx][1] + r)%4)
            case 'F':
                dy, dx = directions[grid[cury][curx][1]]
                r = int(repeat)
            
                for i in range(r):
                    if 0 > cury + dy or cury + dy >= b or 0 > curx + dx or curx + dx >= a:
                        string = string = f"Robot {robot} crashes into the wall"
                        break
                    if grid[cury + dy][curx + dx] != None:
                        string =  f"Robot {robot} crashes into robot {grid[cury + dy][curx + dx][0]}"
                        break
                    else:
                        temp = grid[cury][curx]
                        grid[cury][curx] = None
                        grid[cury + dy][curx + dx] = temp
                        positions[int(robot)] = (cury + dy, curx + dx)
                        cury += dy
                        curx += dx
                    
    if string == "":
        return "OK"
    return string
k = int(input())

for i in range(k):
    a, b = map(int, input().split())
    n, m = map(int, input().split())
    print(solve(a, b, n, m))