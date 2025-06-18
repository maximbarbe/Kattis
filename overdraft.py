n = int(input())
res = 0
bal = 0
for i in range(n):
    bal += int(input())
    if bal < 0 and -bal > res:
        res = -bal
print(res)