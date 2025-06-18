import math
n = int(input())
for i in range(n):
    x = int(input())
    print(str(math.factorial(x))[-1])