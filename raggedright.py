import sys
from math import inf
max_length = -inf
lines = []
for line in sys.stdin:
    line = line.strip("\n")
    if len(line) > max_length:
        max_length = len(line)
    lines.append(line)
    
res = 0
for i in range(len(lines) - 1):
    res += (len(lines[i]) - max_length)**2
print(res)