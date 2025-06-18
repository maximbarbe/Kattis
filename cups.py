n = int(input())
cups = []
for i in range(n):
    data = input()
    if data[0].isnumeric():
        diameter, color = data.split(" ")
        radius = int(diameter) / 2
    else:
        color, radius = data.split(" ")
        radius = int(radius)
    cups.append((color, radius))
cups.sort(key=lambda x: x[1])
for cup in cups:
    print(cup[0])