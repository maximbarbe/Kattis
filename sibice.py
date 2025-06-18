import math
n, w, h = map(lambda x: int(x), input().split(" "))
diag = math.sqrt(w**2 + h**2)
for i in range(n):
    length = int(input())
    if length <= diag:
        print("DA")
    else:
        print("NE")