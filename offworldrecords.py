n, cur, prev = map(int, input().split(" "))
res = 0
for i in range(n):
    jump = int(input())
    if jump > cur + prev:
        res += 1
        prev = cur
        cur = jump
print(res)