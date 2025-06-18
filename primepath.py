from collections import defaultdict, deque

# miller rabin prime test
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def is_prime(n):
    vals = [2, 3]
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


def diff(prime1, prime2):
    d = 0
    for i in range(4):
        p1 = prime1 % 10
        p2 = prime2 % 10
        if p1 != p2:
            d += 1
        prime1 //= 10
        prime2 //= 10
    return d == 1

edges = defaultdict(lambda:[])
primes = []




for i in range(1001, 10000, 2):
    if is_prime(i):
        primes.append(i)




for i in range(len(primes) - 1):
    for j in range(i + 1, len(primes)):
        if diff(primes[i], primes[j]):
            edges[primes[i]].append(primes[j])
            edges[primes[j]].append(primes[i])

t=  int(input())
for i in range(t):
    src, dest = map(int, input().split())
    visited = defaultdict(lambda:False)
    visited[src] = True
    q = deque([(src, 0)])
    while len(q) != 0:
        prime, c = q.popleft()
        if prime == dest:
            print(c)
            break
        else:
            for d in edges[prime]:
                if not visited[d]:
                    q.append((d, c + 1))
                    visited[d] = True
        
    else:
        print("Impossible")