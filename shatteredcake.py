W = int(input())
n = int(input())
area = 0
for i in range(n):
    x, y = map(int, input().split(" "))
    area += x * y
print(area//W)