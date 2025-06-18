n, m = map(lambda x:int(x), input().split(" "))
for i in range(n):
    m -= int(input())
if m < 0:
    print("Neibb")
else:
    print("Jebb")