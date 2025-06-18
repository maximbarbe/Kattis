categories = input().split(" ")
indices = {categories[i]: i for i in range(len(categories))}
n = int(input())
data = []
for i in range(n):
    data.append(input().split(" "))
t = int(input())
for i in range(t):
    cat = input()
    data.sort(key = lambda el:el[indices[cat]])
    print(" ".join(categories))
    for line in data:
        print(" ".join(map(str, line)))
    if i != t - 1:
        print()