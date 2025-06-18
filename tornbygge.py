from sys import maxsize
n = int(input())
pieces = list(map(int, input().split(" ")))
last_piece = -1 * maxsize

res = 0
for piece in pieces:
    if piece > last_piece:
        res += 1
    last_piece = piece
print(res)