vertical = [False for i in range(8)]
horizontal = [False for i in range(8)]
left_diagonal = [False for i in range(16)]
right_diagonal = [False for i in range(16)]
num_queens = 0
# Right_diagonal = i + j + 1
# left_diagonal = 7 -i + j + 1
for i in range(8):
    row = input()
    for j in range(len(row)):
        if row[j] == "*":
            num_queens += 1
            if horizontal[i] == True:
                print("invalid")
                exit()
            else:
                horizontal[i] = True
            if vertical[j] == True:
                print("invalid")
                exit()
            else:
                vertical[j] = True
            if right_diagonal[i + j + 1] == True:
                print("invalid")
                exit()
            else:
                right_diagonal[i + j + 1] = True
            if left_diagonal[7 - i + j + 1] == True:
                print("invalid")
                exit()
            else:
                left_diagonal[7 - i + j + 1] = True
if num_queens != 8:
    print("invalid")
else:
    print("valid")