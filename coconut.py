from collections import deque



game = deque()
s, n = map(int, input().split(" "))
for i in range(1, n + 1):
    game.append((i, "folded"))
    
cur = 0
while len(game) != 1:
    for i in range(s - 1):
        el = game.popleft()
        game.append(el)
    el = game.popleft()
    if el[1] == "folded":
        game.appendleft((el[0], "fist"))
        game.appendleft((el[0], "fist"))
    elif el[1] == "fist":
        game.append((el[0], "palm"))
    
print(game.pop()[0])