k = int(input())
a = int(input())
b = int(input())
res = []
for i in range(0, k//a + 1):
    temp = k - a*i
    if temp % b == 0:
        res.append((i, temp//b))
print(len(res))
for el in res:
    print(*el)