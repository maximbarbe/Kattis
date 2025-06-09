from sys import maxsize
import heapq
players = []
n = int(input())
for i in range(n):
    name, first, second = input().split(" ")
    first = float(first)
    second = float(second)
    players.append((name, first, second))

players.sort(key=lambda el:el[2])
possible_solutions = []
heap = []
for i in range(n):
    temp = [players[i]]
    sumn = players[i][1]
    j = 0
    while len(temp) != 4:
        if j != i:
            temp.append(players[j])
            sumn += players[j][2]
        j += 1
    heapq.heappush(heap, (sumn, temp))
score, team = heapq.heappop(heap)
print(score)
for player in team:
    print(player[0])