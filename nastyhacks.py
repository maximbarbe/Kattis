n = int(input())
for i in range(n):
    r, e, c = map(lambda x: int(x), input().split(" "))
    if r < e - c:
        print("advertise")
    elif r == e - c:
        print("does not matter")
    else:
        print("do not advertise")