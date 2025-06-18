from collections import defaultdict

n, m = map(int, input().split(" "))
if m == 0:
    print("Jebb")
    exit()
if n == 0:
    print("Neibb")
    exit()
dicts = []
for i in range(n):
    data = [*map(int, input().split(" "))]
    box = defaultdict(lambda:False)
    for i in range(1, len(data)):
        box[data[i]] = True
    dicts.append(box)
    
for i in range(1, m+1):
    for box in dicts:
        if box[i] == True:
            break
    else:
        print("Neibb")
        exit()
else:
    print("Jebb")