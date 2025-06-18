a, b, c = map(int, input().split(" "))
if (b - a) * (c - b) < 0:
    print("turned")
elif c - b == b - a:
    print("cruised")
elif abs(c - b) > abs(b - a):
    print("accelerated")
else:
    print("braked")