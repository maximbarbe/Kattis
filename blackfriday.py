from collections import defaultdict

n = int(input())
rolls = [*map(int, input().split(" "))]
seen = defaultdict(lambda: 0)
for i in range(len(rolls)):
    seen[rolls[i]] += 1
valid = [key for key in seen.keys() if seen[key] == 1]
if len(valid) == 0:
    print("none")
else:
    print(rolls.index(max(valid)) + 1)