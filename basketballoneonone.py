points = {
    "A": 0,
    "B": 0
}

game = input()
for i in range(len(game) // 2):
    points[game[2*i]] += int(game[2*i + 1])
if points["A"] > points["B"]:
    print("A")
else:
    print("B")