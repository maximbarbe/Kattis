res = None
potential = -1
n=  int(input())
grid = []
for i in range(n):
    grid.append([*map(int, input().split())])

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1,n):
            pot = grid[i][j]*grid[j][k]*grid[k][i]
            if pot > potential:
                res = (i,j,k)
                potential = pot
print(*map(lambda el:el+1, res))