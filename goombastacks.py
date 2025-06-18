n = int(input())
cur = 0
for i in range(n):
    g, b = map(int, input().split(" "))
    if cur + g < b:
        print("impossible")
        exit()
    cur += g
print("possible")