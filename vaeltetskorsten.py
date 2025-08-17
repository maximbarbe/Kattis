res = 0
for i in range(int(input())):
    v, y = input().split()
    if y == "nej":
        res = max(res, int(v))
print(res)