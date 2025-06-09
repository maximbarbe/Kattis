from math import floor
numbers = list(map(int, input().split(" ")))
a, b = map(int, input().split(" "))
res = 0
for i in range(5):
    res += numbers[2 * i] * numbers[2 * i + 1]
res = int(res / 5)
print(int(res * a / b))