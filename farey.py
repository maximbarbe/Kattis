from math import sqrt, floor
from collections import defaultdict




# Euler Totient function
def phi(n):
    prime_factors = defaultdict(lambda:0)
    temp = n
    while n % 2 == 0:
        prime_factors[2] += 1
        n //= 2
    for i in range(3, floor(sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factors[i] += 1
            n //= i
        if i > n:
            break
    if n != 1:
        prime_factors[n] += 1
    res = temp
    for key in prime_factors.keys():
        res *= (1 - 1/key)
    return int(res)
            
sum_phis = [0]
for i in range(1, 10001):
    sum_phis.append(sum_phis[-1] + phi(i))
n = int(input())
for i in range(n):
    k, val = map(int, input().split())
    # https://en.wikipedia.org/wiki/Farey_sequence
    # Formula for the length
    print(k, 1 + sum_phis[val])