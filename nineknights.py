def pos_is_valid(current_pos, knights_pos):
    for x, y in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
        if(current_pos[0] + x, current_pos[1] + y) in knights_pos:
            return False
    return True


knights_pos = []
for i in range(5):
    string = input()
    for j in range(5):
        if string[j] == "k":
            knights_pos.append((i, j))

if len(knights_pos) != 9:
    print("invalid")
    exit()
for pos in knights_pos:
    if not pos_is_valid(pos, knights_pos):
        print("invalid")
        exit()
print("valid")