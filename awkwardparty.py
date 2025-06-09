from collections import defaultdict


n = int(input())
awkwardness = n

languages = defaultdict(lambda:[])
vals = [*map(int, input().split(" "))]
for i in range(len(vals)):
    languages[vals[i]].append(i)
    
for val in languages.values():
    for i in range(len(val) - 1):
        if val[i + 1] - val[i]< awkwardness:
            awkwardness = val[i + 1] - val[i]
print(awkwardness)