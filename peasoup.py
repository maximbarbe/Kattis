n = int(input())

for i in range(n):
    k = int(input())
    pea = False
    pancakes = False
    name = input()
    for j in range(k):
        item = input()
        if item == "pea soup":
            pea = True
        elif item == "pancakes":
            pancakes = True
    if pea and pancakes:
        print(name)
        exit()
else:
    print("Anywhere is fine I guess")