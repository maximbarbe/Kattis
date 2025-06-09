from math import dist

m = int(input())
for i in range(m):
    x, y = map(float, input().split(" "))
    lit = False
    n = int(input())
    for j in range(n):
        x1, y1 = map(float, input().split(" "))
        if dist((x, y), (x1, y1)) <= 8:
            lit = True
            
    if lit:
        print("light a candle")
    else:
        print("curse the darkness")
