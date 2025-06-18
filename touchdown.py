n = int(input())
vals = [*map(int, input().split())]

yards = 20
down = 1
yards_gained = 0
for i in range(len(vals)):
    yards_gained += vals[i]
    if yards + yards_gained <= 0:
        print("Safety")
        exit()
    elif yards + yards_gained >= 100:
        print("Touchdown")
        exit()
    if yards_gained >= 10:
        down = 1
        yards += yards_gained
        yards_gained = 0
        continue
    down += 1
    if down == 5 and yards_gained < 10:
        print("Nothing")
        exit()
    
else:
    if yards <= 0:
        print("Safety")
    elif yards >= 100:
        print("Touchdown")
    else:
        print("Nothing")