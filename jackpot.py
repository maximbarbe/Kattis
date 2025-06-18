from math import lcm

t = int(input())
for i in range(t):
    input()
    res = lcm(*map(int, input().split()))
    if res <= 10**9:
        print(res)
    else:
        print("More than a billion.")