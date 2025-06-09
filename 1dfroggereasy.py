n, s, m = input().split(" ")
board = list(map(lambda x: int(x), input().split(" ")))

pos = int(s) - 1
magic_number = int(m)
visited_indices = []
hops = 0
game = True
if board[pos] == magic_number:
    print("magic")
    print(hops)
    game = False
    
while game:
    if pos in visited_indices:
        print("cycle")
        print(hops)
        break
    elif pos < 0:
        print("left")
        print(hops)
        break
    elif pos >= len(board):
        print("right")
        print(hops)
        break
    elif board[pos] == magic_number:
        print("magic")
        print(hops)
        break
    visited_indices.append(pos)
    pos += board[pos]
    hops += 1