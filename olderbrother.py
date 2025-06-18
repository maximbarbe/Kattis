from math import log2, floor, sqrt
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

q = int(input())
if q == 1:
    print("no")
elif is_prime(q):
    print("yes")
else:
    if q % 2 == 0:
        if 2**floor(log2(q)) != q:
            print("no")
        else:
            print("yes")
    else:
        for i in range(3, floor(sqrt(q)) + 1):
            if q % i == 0:
                while q%i == 0:
                    q//= i
                if q != 1:
                    print("no")
                else:
                    print('yes')
                exit()