import sys

for line in sys.stdin.readlines():
    a,b,c = map(int, line.split())
    digits = []
    for i in range(c):
        if b > a:
            a *= 10
        digits.append(a//b)
        a -= b*(a//b)
    print("0.", end="")
    for dig in digits:
        print(dig, end="")
    print()