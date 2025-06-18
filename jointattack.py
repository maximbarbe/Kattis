from math import gcd

n = int(input())
coefficients = [*map(int, input().split(" "))]
numerator = 1
denominator = coefficients[-1]
for i in range(len(coefficients) - 2, -1, -1):
    numerator = coefficients[i] * denominator + numerator
    denominator, numerator = numerator, denominator
denominator, numerator = numerator, denominator
temp = gcd(numerator, denominator)
print(f"{numerator//temp}/{denominator//temp}")