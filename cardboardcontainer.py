from math import sqrt, inf, floor

n = int(input())

min_area = inf

for h in range(1, floor(sqrt(n)) + 1):
    for l in range(1, floor(sqrt(n)) + 1):
        if n % (h * l) == 0:
            w = n//(h*l)
            area = 2 * (h*w + w*l + h*l)
            if area < min_area:
                min_area = area
print(min_area)   