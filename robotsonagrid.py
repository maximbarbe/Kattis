from collections import deque, defaultdict

n = int(input())
dp = [[0 for i in range(n)] for j in range(n)]
MOD = 2**31 - 1
grid = []
for i in range(n):
    grid.append(input())
dp[-1][-1] = 1
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if j != n - 1 and grid[i][j + 1] != "#":
            dp[i][j] += dp[i][j + 1]
        if i != n - 1 and grid[i + 1][j] != "#":
            dp[i][j] += dp[i + 1][j]
        dp[i][j] %= MOD
if dp[0][0] != 0:
    print(dp[0][0])
    exit()
    
q = deque([(0, 0)])
visited = defaultdict(lambda:False)
visited[(0, 0)] = True
while q:
    i, j = q.popleft()
    if (i, j) == (n - 1, n-1):
        print("THE GAME IS A LIE")
        exit()
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= i + di < n and 0 <= j + dj < n and grid[i + di][j + dj] != "#" and not visited[(i + di, j + dj)]:
            visited[(i + di,j + dj)] = True
            q.append((i + di, j + dj))
else:
    print("INCONCEIVABLE")