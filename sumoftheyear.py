n = int(input())
res = 0
cubes = 0
sum = 0
for i in range(1, n+1):
    sum += i
    cubes += i **3
    if sum**2 == cubes:
        res += 1
print(res)