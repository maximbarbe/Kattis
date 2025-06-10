a, b = map(int, input().split())
cur = 1
res = 0
temp = b
while b <= a:
    if a % b == 0:
        res+= 1
    
    b += temp
print(res)