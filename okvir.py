m, n = map(int, input().split(" "))
u, l, r, d = map(int, input().split(" "))
grid = []
for i in range(u + m + d):
    row = []
    if i % 2 == 0:
        if (n + l + r)%2 == 0:
            for i in range((n+l+r)//2):
                row.append("#")
                row.append(".")
            
        else:
            for i in range((n+l+r)//2):
                row.append("#")
                row.append(".")
            row.append("#")
    else:
        if (n + l + r)%2 == 0:
            for i in range((n+l+r)//2):
                row.append(".")
                row.append("#")
        else:
            for i in range((n+l+r)//2):
                row.append(".")
                row.append("#")
            row.append(".")
    grid.append(row)
words = []
for i in range(m):
    words.append(input())
    
for i in range(m):
    for j in range(n):
        grid[u+i][l+j] = words[i][j]
        
for row in grid:
    print("".join(row))