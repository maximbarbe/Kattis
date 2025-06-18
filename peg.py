board = []
for i in range(7):
    board.append(input())
res = 0
for i in range(7):
    for j in range(7):
        if board[i][j] == "o":
            # up (if i - 1>0 then i - 2 is at the least 0)
            if i - 1>0:
                if board[i - 1][j] == "o" and board[i - 2][j] == ".":
                    res += 1
            if i + 1 < 6:
                if board[i + 1][j] == "o" and board[i + 2][j] == ".":
                    res += 1
            if j - 1 > 0:
                if board[i][j - 1] == "o" and board[i][j - 2] == ".":
                    res += 1
            if j + 1 < 6:
                if board[i][j + 1] == "o" and board[i][j + 2] == ".":
                    res += 1
print(res)