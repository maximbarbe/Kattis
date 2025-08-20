from collections import Counter

c = Counter()
cur = Counter()
names = []
for i in range(int(input())):
    s = input().split(" ")
    c[s[0]] += 1
    names.append(" ".join(s))
for n in names:
    if c[n.split(" ")[0]] == 1:
        print(n)
    else:
        parts = n.split(" ")
        print(f"{parts[0]} {cur[parts[0]] + 1}. {' '.join(parts[1:])}")
        cur[parts[0]] += 1
