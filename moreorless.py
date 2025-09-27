import sys

for line in sys.stdin.readlines():
    a, b = map(int, line.split())
    if b <  a:
        print("More")
    elif b > a:
        print("Less")
