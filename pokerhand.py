from collections import defaultdict

ranks = defaultdict(lambda:0)
for card in input().split(" "):
    ranks[card[0]] += 1
print(max(ranks.values()))