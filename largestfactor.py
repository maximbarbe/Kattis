from math import sqrt, floor

factors = set()
n = int(input())
while n % 2 == 0:
    factors.add(2)
    n //= 2
for i in range(3, floor(sqrt(n)) + 1):
    if i > n:
        break
    while n % i == 0:
        factors.add(i)
        n //= i
if n != 1:
    print(n)
else:
    print(max(factors))