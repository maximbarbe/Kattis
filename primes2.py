from math import gcd


# miller rabin prime test
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def is_prime(n):
    vals = [2, 3, 5, 7, 11]
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


t = int(input())
for i in range(t):
    valid = 0
    denom = 0
    num = input()
    for base in [2, 8, 10, 16]:
        try:
            temp = int(num, base)
            denom += 1
            if temp in [0 ,1]:
                continue
            if is_prime(temp):
                valid += 1
        except:
            continue
    
    
    
    if valid == 0:
        print("0/1")
    else:
        g = gcd(valid, denom)
        print(f"{valid//g}/{denom//g}")