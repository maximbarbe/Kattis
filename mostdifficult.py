# miller rabin prime test
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def is_prime(n):
    temp = n- 1
    s, d = 0, 0
    while temp % 2 == 0:
        s += 1
        temp //= 2
    d = temp

    vals = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    if n in vals:
        return True
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

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
for i in range(25, 5000, 2):
    if is_prime(i):
        primes.append(i)

q = int(input())
for i in range(q):
    n = int(input())
    if n% 2 == 1:
        if is_prime(n + 2):
            print(2)
        else:
            print(-1)
    else:
        for j in range(1, len(primes)):
            if is_prime(n + primes[j]):
                print(primes[j])
                break