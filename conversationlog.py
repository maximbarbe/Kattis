from collections import Counter, defaultdict

n = int(input())

frequencies = Counter()

said = defaultdict(lambda:set())

for i in range(n):
    words = input().split()
    frequencies.update(words[1:])
    said[words[0]].update(words[1:])
vals = list(said.values())
for i in range(1, len(vals)):
    vals[0] = vals[0].intersection(vals[i])
if len(vals[0]) == 0:
    print("ALL CLEAR")
else:
    vals[0] = list(vals[0])
    vals[0].sort(key=lambda el:(-frequencies[el], el))
    for word in vals[0]:
        print(word)