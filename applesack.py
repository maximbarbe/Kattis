n, k = map(int, input().split())

res = 0
while n != 0:
    res += 1
    if n % k == 0:
        n -= n//k
    else:
        n -= n//k
        n -= 1
print(res + 1)