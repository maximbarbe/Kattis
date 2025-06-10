length = len(input().split(" ")) - 1
n = int(input())
A = []
B = []
players = []
for i in range(n):
    players.append(input())
cur = 0
to_a = True
while players != []:
    cur = (cur + length)%len(players)
    if to_a:
        A.append(players[cur])
    else:
        B.append(players[cur])
    players.pop(cur)
    if len(players) == 0:
        break
    cur %= len(players)
    to_a ^= True
    
print(len(A))
for i in range(len(A)):
    print(A[i])
print(len(B))
for i in range(len(B)):
    print(B[i])