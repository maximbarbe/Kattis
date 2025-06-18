from math import factorial, log2

m, n, t = map(int, input().split(" "))
if t == 1:
    if 2**n > m or factorial(n) > m:
        print("TLE")
    else:
        print("AC")
elif t== 2:
    if 2**n > m:
        print("TLE")
    else:
        print("AC")
elif t == 3:
    if n**4 > m:
        print("TLE")
    else:
        print("AC")
elif t == 4:
    if n ** 3 > m:
        print("TLE")
    else:
        print("AC")
elif t == 5:
    if n ** 2 > m:
        print("TLE")
    else:
        print("AC")
elif t == 6:
    if n * log2(n) > m:
        print("TLE")
    else:
        print("AC")
else:
    if n > m:
        print("TLE")
    else:
        print("AC")