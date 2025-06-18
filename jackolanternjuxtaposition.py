n = list(map(lambda x:int(x), input().split(" ")))
res = 1
for i in range(len(n)):
    res *= n[i]
print(res)