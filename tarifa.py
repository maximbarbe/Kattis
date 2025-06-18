x = int(input())
n = int(input())
res = 0
for i in range(n):
    res += x
    res -= int(input())
print(res + x)