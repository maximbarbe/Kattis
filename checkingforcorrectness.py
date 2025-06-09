import sys

for line in sys.stdin:
    a, op, b = line.split()
    a = int(a)
    b = int(b)
    match op:

        case '+':
            print((a%10000 + b %10000)%10000)
        case '*':
            print((a%10000 * b %10000)%10000)
        case _:
            print(pow(a, b, 10000))