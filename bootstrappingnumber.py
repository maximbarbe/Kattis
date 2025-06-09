import decimal
from decimal import Decimal

decimal.getcontext().prec = 100
start, end = 1, 10
n = int(input())
while True:
    mid = Decimal((start+end)/2)
    res = mid**mid - n
    if abs(res) <= 0.00000005:
        print(mid)
        exit()
    elif res < 0:
        start = mid
    else:
        end = mid