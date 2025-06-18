import sys

numbers = [0, 1, 2, 5, 9, 8, 6]



for line in sys.stdin:
    line = int(line)
    c = []
    while line != 0:
        c.append(str(numbers[line%7]))
        line //= 7
    print("".join(c))