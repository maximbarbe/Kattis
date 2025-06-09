"""
1-2
2-4
3-6
4-9
5-12
6-16

"""
from math import floor
n = int(input())
if n == 1:
    print(2)
else:
    if n % 2 == 0:
        print((n-(n-2)//2)**2)
    else:
        print((n + 1 - (n-1)//2)**2 - (n+3)//2)