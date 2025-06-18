import sys
from collections import defaultdict
names = []

firsts = defaultdict(lambda:0)
for line in sys.stdin:
    first, last = line.rstrip().split(" ")
    names.append((first, last))
    firsts[first] += 1

    
names.sort(key=lambda el:(el[1], el[0]))
for i in range(len(names)):
    if firsts[names[i][0]] == 1:
        print(names[i][0])
    else:
        print(" ".join(names[i]))