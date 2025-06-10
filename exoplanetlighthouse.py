from math import acos

n = int(input())
# Formula source: https://en.wikipedia.org/wiki/Horizon#Distance_to_the_horizon
for i in range(n):
    r, h1, h2 = map(float, input().split())
    s1 = r*acos(r/(r+h1/1000))
    s2 = r*acos(r/(r+h2/1000))
    print(s1 + s2)