from collections import Counter
counter = Counter(input())
odds = set()
for el in counter.elements():
    if counter[el] % 2 == 1:
        odds.add(el)
res = 0
if len(odds) > 1:
    print(len(odds) - 1)
else:
    print(0)