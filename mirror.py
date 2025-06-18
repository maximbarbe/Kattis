t = int(input())

for _ in range(t):
    r,c=map(int, input().split())
    new_grid = [[None for i in range(c)] for j in range(r)]
    for i in range(r):
        row = input()
        for j in range(len(row)):
            new_grid[r-i-1][c-j-1] = row[j]
    print("Test", _+ 1)
    for row in new_grid:
        print("".join(row))