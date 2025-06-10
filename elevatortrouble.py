f, s, g, u, d= map(int, input().split())

if s == g:
    print(0)
    exit()
elif g < s:
    s, g = g, s
    u, d =d, u

if d == 0:
    if u == 0:
        print("use the stairs")
        exit()
    x = (g-s)//u
    if u * x != g - s:
        print("use the stairs")
    else:
        print(x)
    exit()
for i in range(f):
    y =(i * u - g + s)/d
    if y >= 0:
        if (abs(y - round(y))) < 0.0000001:
            print(i + round(y))
            exit()
else:
    print("use the stairs")