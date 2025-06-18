def SSD(b, n):
    max_base = 0
    while b ** (max_base + 1) <= n:
        max_base += 1
    res = 0
    for i in range(max_base, -1, -1):
        res += (n // b**i)**2
        n -= (n // b**i)*b**i
    return res
        

N = int(input())
for i in range(N):
    k, b, n = map(int, input().split(" "))
    print(f"{k} {SSD(b, n)}")