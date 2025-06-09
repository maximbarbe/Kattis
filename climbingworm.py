a, b, h = map(int, input().split(" "))

res = 0
cur = 0
while True:
    cur += a
    res += 1
    if cur >= h:
        break
    cur -= b
    
print(res)