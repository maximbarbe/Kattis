from collections import defaultdict
n = int(input())
kattis = defaultdict(lambda:0)
dom = defaultdict(lambda:0)
for i in range(n):
    kattis[input()] += 1
for i in range(n):
    dom[input()] += 1
res = 0

for key in kattis.keys():
    res += min(kattis[key], dom[key])
print(res)