import sys
from collections import Counter

for line in sys.stdin:
    prev = None
    c = 0
    for char in line.rstrip():
        if char != prev:
            if prev != None:
                print(f"{c}{prev}", end="")
                prev = char
                c = 1
            else:
                prev = char
                c = 1
        else:
            c += 1
    else:
        print(f"{c}{prev}")  