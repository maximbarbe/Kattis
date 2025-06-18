n = int(input())
m = int(input())
rooms = []
for i in range(n):
    rooms.append("")
for i in range(m):
    rooms[i % n] += "*"
for room in rooms:
    print(room)