def digits(n):
    if n == 0:
        return 1
    cur = 0
    while n != 0:
        cur += 1
        n //= 10
    return cur
n = int(input())
for i in range(n):
    print(digits(int(input())))