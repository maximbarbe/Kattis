from itertools import permutations, combinations


# miller rabin prime test
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def is_prime(n):
    if n == 1 or n % 2 == 0 and n != 2:
        return False
    temp = n- 1
    s, d = 0, 0
    while temp % 2 == 0:
        s += 1
        temp //= 2
    d = temp

    vals = [2, 3, 5]
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

t = int(input())
for i in range(t):
    digits = [dig for dig in input()]
    res = 0
    primes = set()
    for i in range(1, len(digits) + 1):
        for comb in combinations(digits, i):
            for perm in set(permutations(comb)):
                num =int("".join(perm))
                if is_prime(num):
                    primes.add(num)
    print(len(primes))