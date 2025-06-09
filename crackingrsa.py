# Source for Miller Rabin
#https://fr.wikipedia.org/wiki/Test_de_primalit%C3%A9_de_Miller-Rabin
def miller_rabin(n):
    s, d = 0, 0
    k = n - 1
    while k % 2 == 0:
        s += 1
        k//=2
    d = k
    vals = [2, 3]
    for a in vals:
        x = pow(a, d, n)
        for i in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
        if y != 1:
            return False
    return True
    


T = int(input())
for i in range(T):
    n, e = map(int, input().split(" "))
    # find two primes such that p*q = n
    if n % 2 == 0:
        p = 2
        q = n // 2
    else:
        primes = [3]
        for i in range(5, 1000, 2):
            if miller_rabin(i):
                primes.append(i)
        p = None
        q = None
        for i in range(len(primes) - 1):
            for j in range(i + 1, len(primes)):
                if primes[i] * primes[j] == n:
                    p = primes[i]
                    q = primes[j]
            if p != None:
                break
    phi = (p-1)*(q-1)
    d = 1
    while True:
        if (d*e - 1)%phi == 0:
            print(d)
            break
        d += 1