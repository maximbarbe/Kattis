def sum_digits(n):
    cur = 0
    while n != 0:
        cur += n % 10
        n //= 10
    return cur
while True:
    N = int(input())
    if N == 0:
        break
    p = 11
    sum_digits_N = sum_digits(N)
    while True:
        if sum_digits(N * p) == sum_digits_N:
            print(p)
            break
        p += 1
    