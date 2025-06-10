# Miller rabin primality test
# SRC: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def is_prime(n):
    vals = [2, 3, 5, 7]
    if n in vals:
        return True
    if n % 2 == 0:
        return False
    temp = n - 1
    s = 0
    while temp % 2 == 0:
        s += 1
        temp //= 2
    d = temp
    for a in vals:
        x = pow(a, d, n)
        for i in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x= y
        if y != 1:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    n_prime = is_prime(n)
    start = 2*n + 1
    while True:
        if is_prime(start):
            break
        start += 2
    if not n_prime:
        print(f"{start} ({n} is not prime)")
    else:
        print(f"{start}")