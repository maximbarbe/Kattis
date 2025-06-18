r,d = map(int, input().split())
if r == 1 and d == 1:
    print(0)
    exit()
if r == 1:
    print(2*d - 2)
    exit()
if d == 1:
    print(2*r - 2)
    exit()
if r % 2 == 0 or d % 2 == 0:
    print(r*d)
else:
    print(r*d + 1)