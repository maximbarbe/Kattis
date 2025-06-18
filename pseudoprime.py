# miller rabin prime test
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def is_prime(n):
    vals = [2, 3, 5, 7]
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

while True:
    p, a = map(int, input().split())
    if is_prime(p):
        print("no")
        continue
    if p == 0 and a == 0:
        break
    if pow(a, p, p) == a:
        print("yes")
    else:
        print("no")