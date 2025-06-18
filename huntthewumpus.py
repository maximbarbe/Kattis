from math import floor, dist, inf

wumpuses = set()
seed = int(input())

while len(wumpuses) != 4:
    seed = seed + floor(seed/13) + 15
    y = seed % 10
    temp = seed // 10
    x = temp % 10
    wumpuses.add((x, y))
moves = 0
while True:

    x, y = map(int, [*input().rstrip()])
    moves += 1

    if (x, y) in wumpuses:
        wumpuses.remove((x, y))
        print("You hit a wumpus!")
    min_dist = inf
    if len(wumpuses) != 0:
        for x1, y1 in wumpuses:
            if abs(x1 - x) + abs(y1 - y) < min_dist:
                min_dist = abs(x1 - x) + abs(y1 - y)
                
        print(min_dist)
    else:
        print(f"Your score is {moves} moves.")
        exit()