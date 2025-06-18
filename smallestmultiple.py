from math import lcm
import sys
for line in sys.stdin:
    vals = [*map(int, line.split(" "))]
    print(lcm(*vals))
