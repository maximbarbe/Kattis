a, b, c, d = map(int, input().split(" "))
vals = [*map(int, input().split(" "))]
for i in range(len(vals)):
    if (vals[i] - 1)% (a + b) >=  a and (vals[i]-1) % (c + d) >= c:
        print("none")
    elif (vals[i]-1) % (a + b) >= a or (vals[i]-1) % (c + d) >= c:
        print("one")
    else:
        print("both")