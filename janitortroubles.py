from math import sqrt
a, b, c, d = map(int, input().split(" "))
res = sqrt(((a + b + c + d) / 2 - a)*((a + b + c + d) / 2 - b) * ((a + b + c + d) / 2 - c) * ((a + b + c + d) / 2 - d))
print(round(res, 6))