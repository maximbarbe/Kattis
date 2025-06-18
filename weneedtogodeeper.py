y = int(input())
res = 0
for w in range(4, 24):
    for h in range(5, 24):
        if 2*w + 2*(h-2) <= y:
            res += 1
print(res)