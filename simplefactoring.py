from math import sqrt
n = int(input())
for i in range(n):
    a, b,c = map(int, input().split(" "))
    delta = b**2 - 4 * a * c
    if ( delta >= 0 and int(sqrt(delta)) == sqrt(delta)):
        print("YES")
    else:
        print("NO")