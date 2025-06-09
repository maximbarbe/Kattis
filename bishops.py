import sys
for line in sys.stdin:
    n = int(line)
    if n in [0, 1]:
        print(n)
    else:
        print(2*n - 2)