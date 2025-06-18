moves = input()
cur = 1
for char in moves:
    if char == "A":
        if cur == 1:
            cur = 2
        elif cur == 2:
            cur = 1
    elif char == "B":
        if cur == 2:
            cur = 3
        elif cur == 3:
            cur = 2
    else:
        if cur == 1:
            cur = 3
        elif cur == 3:
            cur = 1
print(cur)