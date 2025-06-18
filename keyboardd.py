from collections import Counter


c1 = Counter(input())
c2 = Counter(input())
print("".join([key for key in c1.keys() if c2[key] != 0 and c1[key] != c2[key]]))