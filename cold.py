n = int(input())
res = 0
temps = list(map(lambda x:int(x), input().split(" ")))
for i in range(len(temps)):
    if temps[i] < 0:
        res += 1
print(res)