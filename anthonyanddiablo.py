from math import pi

A, N = map(float, input().split(" "))
if A > N or 2*(pi*A)**(1/2) > N:
    print("Need more materials!")
else:
    print("Diablo is happy!")