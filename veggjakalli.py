n, m = map(int, input().split(" "))
string = input()
walls = [0]
if n in [1, 2]:
    print("Neibb")
else:
    for i in range(n):
        if string[i] == "#":
            walls.append(walls[i] + 1)
        else:
            walls.append(walls[i])
    res = 1000000
    for i in range(0, n-(m + 1)):
        if string[i] == "#" and string[i + m + 1] == "#":
            count = walls[i + m + 1] - walls[i] - 1
            if count < res:
                res = count
                
    if res == 1000000:
        print("Neibb")
    else:
        print(res)