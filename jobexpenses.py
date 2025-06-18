n = int(input())

res = 0
if n == 0:
    print(0)
    exit()
for num in list(map(int, input().split(" "))):
    if num < 0:
        res += num
print(abs(res))