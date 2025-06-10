from collections import Counter
s = input()
c = Counter(s)
if len(c.keys()) == 3 and s.startswith("b") and c["b"] == 1 and s[-1] in "aeiouy" and c[s[-1]] == 1 and c["r"] >= 2:
    print("Jebb")
else:
    print("Neibb")