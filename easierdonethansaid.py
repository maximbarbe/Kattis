import sys
from collections import defaultdict

vowels = defaultdict(lambda:False)
for c in "aeiou":
    vowels[c] = True
for line in sys.stdin.readlines():
    line = line.rstrip()
    if line == "end":
        break
    res = True
    v = False
    for i in range(len(line)):
        v |= vowels[line[i]]
        if i + 2 < len(line):
            if vowels[line[i]] == vowels[line[i + 1]] and vowels[line[i]] == vowels[line[i + 2]]:
                res = False
                break
        if i + 1 < len(line):
            if line[i] == line[i + 1] and line[i] not in "eo":
                res = False
                break
    
    print(f"<{line}> is {('not ', '')[res and v]}acceptable.")
    
    
    
