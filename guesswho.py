n, m, q = map(int, input().split(" "))
grid = []
for i in range(n):
    grid.append(input())
board = grid.copy()
for i in range(q):
    idx, res = input().split(" ")
    idx = int(idx) - 1
    board = [board[j] for j in range(len(board)) if board[j][idx] == res]
    
if len(board) == 1:
    print("unique")
    print(grid.index(board[0]) + 1)
else:
    print("ambiguous")
    print(len(board))