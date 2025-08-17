from math import ceil

s, n = input().split()
n = int(n)
if s == "residential":
    if n == 1:
        print(0)
    else:
        print(ceil(n/5))
elif s == "commercial":
    if n == 1:
        print(0)
    else:
        print(ceil(n/7))
else:
    if n == 1:
        print(0)
    else:
        print(ceil(n/4))