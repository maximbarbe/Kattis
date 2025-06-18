from collections import defaultdict
n, m = map(int, input().split())
hunter = defaultdict(lambda:False)
cheaters = set()
players = input().split()
hunter[players[0]] = True
for i in range(m):
    tags, tagged = input().split(" tar ")
    if hunter[tags] == False:
        cheaters.add(tags)
    hunter[tags] = False
    hunter[tagged] = True
print(len(cheaters))
print(*sorted(cheaters))