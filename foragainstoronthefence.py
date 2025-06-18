xv, yv = map(int, input().split())
xp, yp = map(int, input().split())
u = int(input())
d = (xv-xp)**2 + (yv-yp)**2
if d < u:
    print("for")
elif d > u:
    print("against")
else:
    print("on the fence")