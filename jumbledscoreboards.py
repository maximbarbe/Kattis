t = int(input())
preva, prevb = 0,0
for i in range(t):
    a, b = map(int, input().split())
    if a >= preva and b >= prevb:
        preva = a
        prevb = b
    else:
        print("no")
        exit()
print("yes")