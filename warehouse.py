from collections import defaultdict

t = int(input())
for i in range(t):
    n = int(input())
    rank = defaultdict(lambda:0)
    for j in range(n):
        data = input().split(" ")
        rank[data[0]] += int(data[1])
    print(len(rank.keys()))
    for key, val in sorted(rank.items(), key = lambda el: (-el[1], el[0])):
        print(f"{key} {val}")