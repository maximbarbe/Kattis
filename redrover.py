from collections import Counter

c = Counter()
s = input()
res = 100
for i in range(1, len(s) + 1):
    for j in range(len(s) - i + 1):
        c[s[j:j+i]] += 1
for _, count in c.most_common():
    if len(_) == 1:
        res = min(res, len(s))
        continue
    temp = s
    res = min(res, len(_) +len(s.replace(_, "m")))
print(res)