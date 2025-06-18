from math import prod, gcd

n = int(input())
n_vals = map(int, input().split())
m = int(input())
m_vals = map(int, input().split())
res = str(gcd(prod(n_vals), prod(m_vals)))
print(res[-9:])