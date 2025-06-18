# miller rabin prime test
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def is_prime(n):
    vals = [2, 7, 61]
    if n in vals:
        return True
    if n % 2 == 0:
        return False
    temp = n- 1
    s, d = 0, 0
    while temp % 2 == 0:
        s += 1
        temp //= 2
    d = temp


    for a in vals:
        x = pow(a, d, n)
        for i in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n -1:
                return False
            x = y
        if y != 1:
            return False
    return True

primes = [2]
cur = 3
while len(primes) != 100:
    if is_prime(cur):
        primes.append(cur)
    cur += 2
for p in primes:
    print(p) 