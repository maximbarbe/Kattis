n, k = map(int, input().split(" "))
res = 0
for i in range(n):
    res += k - len(set(input().split(" ")))
print(res)