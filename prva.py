n, m = map(int, input().split(" "))
grid = [["#" for i in range(m + 2)]]
words = []
for i in range(n):
    grid.append(["#"]+ [char for char in input()] + ["#"])
grid.append(["#" for i in range(m + 2)])
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (grid[i - 1][j] == "#"):
            word = ""
            cur = i
            while grid[cur][j] != "#":
                word += grid[cur][j]
                cur += 1
            if len(word) >= 2:
                words.append(word)
        if (grid[i][j - 1] == "#"):
            word = ""
            cur = j
            while grid[i][cur] != "#":
                word += grid[i][cur]
                cur += 1
            if len(word) >= 2:
                words.append(word)
            
words.sort()
print(words[0])