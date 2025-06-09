import sys

for line in sys.stdin:
    print(f"{eval(line.rstrip()):.2f}")