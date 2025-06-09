from collections import defaultdict
from math import inf
friends = defaultdict(lambda: (-1 * inf, None))
n = int(input())
for i in range(n):
    data = input().split(" ")
    if friends[data[2]][0] < int(data[1]):
        friends[data[2]] = (int(data[1]), data[0])
print(len(friends.keys()))
names = []
for key in friends.keys():
    names.append(friends[key][1])
names.sort()
for name in names:
    print(name)