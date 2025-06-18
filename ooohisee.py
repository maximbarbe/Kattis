r,c=map(int,input().split())
grid=[]
for i in range(r):
    grid.append(input())
pos=[]
for i in range(1, r-1):
    for j in range(1,c-1):
        if grid[i][j] == "0" and grid[i + 1][j] == grid[i - 1][j] == grid[i][j + 1] == grid[i][j - 1] == grid[i + 1][j + 1] == grid[i + 1][j - 1] == grid[i - 1][j + 1] == grid[i - 1][j - 1] == "O":
            pos.append((i,j))
if not pos:
    print("Oh no!")
elif len(pos) != 1:
    print(f"Oh no! {len(pos)} locations")
else:
    print(*map(lambda el:el + 1,pos[0]))