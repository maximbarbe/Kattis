from collections import defaultdict

freq = defaultdict(lambda:0)
n, c = map(int, input().split(" "))
vals = [*map(int, input().split(" "))]
res = []
for i in range(len(vals)):
    freq[vals[i]] += 1
for key, val in sorted(freq.items(), key=lambda el:el[1], reverse=True):
    res += [key for i in range(val)]
print(" ".join(map(str, res)))