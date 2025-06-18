e, f, c = map(int, input().split(" "))
res = 0
cur = e + f
while (cur >= c):
    res += cur // c
    cur = cur % c + cur // c
    
print(res)