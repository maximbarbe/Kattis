n, p , m = map(int, input().split(" "))
scores = {}
won = {}
winners = []
for i in range(n):
    name = input()
    scores[name] = 0
    won[name] = False
for i in range(m):
    name, points = input().split(" ")
    points = int(points)
    scores[name] += points
    if scores[name] >= p and won[name] == False:
        winners.append(name)
        won[name] = True
        
if len(winners) == 0:
    print("No winner!")
else:
    for name in winners:
        print(f"{name} wins!")