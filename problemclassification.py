from collections import defaultdict


n = int(input())
count = dict()

edges = defaultdict(lambda:[])

for i in range(n):
    data = input().split()
    count[data[0]] = 0
    for word in data[2:]:
        edges[word].append(data[0])
    
while True:
    try:
        line = input().split()
    except EOFError:
        break
    for word in line:
        for edge in edges[word]:
            count[edge] += 1

res = []
max_value = max(count.values())
for key, val in count.items():
    if val == max_value:
        res.append(key)
res.sort()
for el in res:
    print(el)