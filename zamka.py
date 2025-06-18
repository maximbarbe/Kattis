import math
def sum_digits(num):
    cur = 0
    while num != 0:
        cur += num % 10
        num //= 10
    return cur
L = int(input())
D = int(input())
X = int(input())
min = math.inf
max = -1 * math.inf
for i in range(L, D + 1):
    if sum_digits(i) == X:
        if i > max:
            max = i
        if i < min:
            min = i
print(min)
print(max)