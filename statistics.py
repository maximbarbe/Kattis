import sys

num = 1
for line in sys.stdin:
    line = line.strip("\n")
    data = [*map(int, line.split(" "))][1:]
    maximum = max(data)
    minimum = min(data)
    ran = maximum - minimum
    print(f"Case {num}: {minimum} {maximum} {ran}")
    num += 1