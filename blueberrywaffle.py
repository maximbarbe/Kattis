r,f = map(int, input().split(" "))
if (f % r) == 0:
    if (f//r)%2 == 0:
        print("up")
    else:
        print("down")
else:
    if (f//r) % 2 == 0:
        if (f%r) < (r//2):
            print("up")
        else:
            print("down")
    else:
        if (f%r) < (r//2):
            print("down")
        else:
            print("up")