n = int(input())
if n % 100 != 0:
    n -= n % 100
    n += 100
res = 0
res += n//500
n -= 500 * (n//500)
res += n//200
n -= 200 * (n//200)
res += n//100
print(res)