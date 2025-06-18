from collections import defaultdict


available = defaultdict(lambda:[0, 0, 0])
taken = defaultdict(lambda: [0, 0])
n = int(input())
for i in range(n):
    color, type, quant = input().split()
    if type == "any":
        available[color][0] += int(quant)
    elif type == "left":
        available[color][1] += int(quant)   
    else:
        available[color][2] += int(quant)

for val in available.values():
    if val[0] >= 1 and (val[1] >= 1 or val[2] >= 1) or val[1] >= 1 and val[2] >= 1 or val[0] >= 2:
        break
else:
    print("impossible")
    exit()
res = 0
for key, val in available.items():
    if val[1] == 0 and val[2] == 0:
        res += 1
        available[key][0] -= 1
    else:
        if val[1] >= val[2]:
            res += val[1]
            available[key][1] = 0
        else:
            res += val[2]
            available[key][2] = 0
print(res + 1)