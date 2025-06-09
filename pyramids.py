n = int(input())
res = 0
cur = 1
while n > 0:
    if n - cur**2 < 0:
        print(res)
        exit()
    else:
        n -= cur ** 2
        cur += 2
        res += 1
print(res)