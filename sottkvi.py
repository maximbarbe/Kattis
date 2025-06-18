n, k, day = map(int, input().split(" "))
res = 0
for i in range(n):
    if int(input()) + 14 <= day + k:
        res += 1
print(res)