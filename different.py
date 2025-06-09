import sys
for line in sys.stdin:
    A, B = map(lambda x: int(x), line.split(" "))
    print(abs(A - B))