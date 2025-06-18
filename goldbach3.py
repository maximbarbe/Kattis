# miller rabin prime test
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def is_prime(n):
    temp = n- 1
    s, d = 0, 0
    while temp % 2 == 0:
        s += 1
        temp //= 2
    d = temp

    vals = [2, 3, 5, 7]
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


n = int(input())
if n == 7:
    print(2, 2, 3)
    exit()

factors = []
factors.append(3)
n -= 3

for i in range(3, n//2 + 1, 2):
    if is_prime(i) and is_prime(n-i):
        print(*factors, i, n-i)
        exit()