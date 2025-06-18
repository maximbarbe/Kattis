from collections import defaultdict
from random import choice
names = []
seen = defaultdict(lambda:False)
vowels = "aeiou"
n = int(input())
consonants = "bcdfghjklmnpqrstvwxz"
while len(names) != n:
    name = []
    for i in range(10):
        name.append(choice(vowels))
        name.append(choice(consonants))
    name = "".join(name)
    if not seen[name]:
        names.append(name)
        seen[name] = True
for n in names:
    print(n)