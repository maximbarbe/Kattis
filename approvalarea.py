from math import pi
from decimal import getcontext, Decimal



getcontext().prec = 100
u = int(input())
print(Decimal(u)*Decimal(pi))