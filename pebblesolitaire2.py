from math import inf
from functools import lru_cache

@lru_cache(None)
def backtrack(board):
    board = [*board]
    cur = inf
    for i in range(len(board) - 2):
        if board[i] == 'o' and board[i + 1] == "o" and board[i + 2] == "-":
            board[i] = "-"
            board[i + 1] = "-"
            board[i + 2] = "o"
            cur = min(cur, backtrack("".join(board)))
            board[i] = "o"
            board[i + 1] = "o"
            board[i + 2] = "-"
    for i in range(len(board) -1, 1, -1):
        if board[i] == 'o' and board[i - 1] == "o" and board[i - 2] == "-":
            board[i] = "-"
            board[i - 1] = "-"
            board[i - 2] = "o"
            cur = min(cur, backtrack("".join(board)))
            board[i] = "o"
            board[i - 1] = "o"
            board[i - 2] = "-"
    return min(cur, board.count("o"))


n = int(input())
for i in range(n):
    
    print(backtrack(input()))