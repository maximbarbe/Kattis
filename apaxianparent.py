Y, P = input().split(" ")
if Y.endswith("ex"):
    print("".join([Y, P]))
elif Y.endswith("e"):
    print("".join([Y, "x", P]))
elif Y[-1] in "aiou":
    print("".join([Y[:len(Y) - 1], "ex", P]))
else:
    print("".join([Y, "ex", P]))