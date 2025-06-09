from collections import defaultdict
while True:
    n = int(input())
    if n == 0:
        break
    ingredients = defaultdict(lambda: [])
    for i in range(n):
        line = input().split(" ")
        for j in range(1, len(line)):
            ingredients[line[j]].append(line[0])
    keys = list(ingredients.keys())
    keys.sort()
    for key in keys:
        print(f"{key} {' '.join(sorted(ingredients[key]))}")