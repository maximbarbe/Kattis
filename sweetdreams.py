from math import dist
x, y = map(int, input().split())
n = int(input())
res = True
for i in range(n):
    x1, y1 = map(int, input().split())
    res = res and dist((x, y), (x1, y1)) >8
print(("NO","YES")[res])