x, y = map(int, input().split(" "))
if x == 0 and y == 0:
    print("Not a moose")
elif x == y:
    print(f"Even {x+y}")
else:
    print(f"Odd {2*max(x, y)}")