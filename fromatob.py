a, b = map(int, input().split())
res = 0

while a > b:
    res += 1
    if a % 2 == 1:
        a += 1
    else:
        a //= 2
    
if a < b:
    res += b - a
    
print(res)