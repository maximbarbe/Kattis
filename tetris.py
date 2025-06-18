columns, piece = map(int, input().split(" "))
vals = list(map(int, input().split(" ")))
if piece == 1:
    res = columns
    for i in range(columns - 3):
        if vals[i] == vals[i+1] ==  vals[i + 2] == vals[i + 3]:
            res += 1
    print(res)
    exit()
elif piece == 2:
    res = 0
    for i in range(columns - 1):
        if vals[i] == vals[i + 1]:
            res += 1
    print(res)
    exit()
elif piece == 3:
    res = 0
    for i in range(columns - 2):
        if vals[i] == vals[i + 1] == vals[i + 2] - 1:
            res += 1
    for i in range(columns - 1):
        if vals[i] - 1 == vals[i + 1]:
            res += 1
    print(res)
    exit()
elif piece == 4:
    res = 0
    for i in range(columns - 2):
        if vals[i] - 1 == vals[i + 1] == vals[i + 2]:
            res +=  1
    for i in range(columns - 1):
        if vals[i] == vals[i + 1] - 1:
            res += 1
    print(res)
    exit()
elif piece == 5:
    res = 0
    for i in range(columns - 2):
        if vals[i] == vals[i + 1] == vals[i + 2]:
            res += 1
    for i in range(columns - 1):
        if vals[i] == vals[i +1] - 1:
            res += 1
    for i in range(columns -1):
        if vals[i] - 1 == vals[i + 1]:
            res +=  1
    for i in range(columns - 2):
        if vals[i] - 1 == vals[i + 1] == vals[i + 2] - 1:
            res += 1
    print(res)
    exit()
elif piece == 6:
    res = 0
    for i in range(columns - 2):
        if vals[i] == vals[i + 1] == vals[i + 2]:
            res += 1
    for i in range(columns - 1):
        if vals[i] == vals[i + 1]:
            res += 1
    for i in range(columns - 2):
        if vals[i] == vals[i + 1] - 1 == vals[i + 2] - 1:
            res += 1
    for i in range(columns - 1):
        if vals[i] - 2 == vals[i + 1]:
            res += 1
    print(res)
    exit()
elif piece == 7:
    res = 0
    for i in range(columns - 2):
        if vals[i] == vals[i + 1] == vals[i + 2]:
            res += 1
    for i in range(columns - 1):
        if vals[i] == vals[i + 1] - 2:
            res += 1
    for i in range(columns - 2):
        if vals[i] - 1 == vals[i + 1] - 1 == vals[i + 2]:
            res += 1
    for i in range(columns - 1):
        if vals[i] == vals[i + 1]:
            res += 1
    print(res)
    exit()