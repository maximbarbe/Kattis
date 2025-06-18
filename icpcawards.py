from collections import OrderedDict

univ = OrderedDict()
n = int(input())
for i in range(n):
    uni, name = input().split(" ")
    if uni not in univ.keys():
        univ[uni] = []
    univ[uni].append(name)

cur = 1
for key in univ.keys():
    if cur > 12:
        break
    print(f"{key} {univ[key][0]}")
    cur += 1