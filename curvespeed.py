from math import sqrt
import sys
for line in sys.stdin:
    R, S = map(float, line.rstrip().split())

    print(int(round(sqrt((R  * (S + 0.16))/0.067))))