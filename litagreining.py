r, g, b = map(int, input().split())
if r > g and r > b:
    print("raudur")
elif g > r and g > b:
    print("graenn")
elif b > r and b > g:
    print("blar")
elif r == g and b < r:
    print("gulur")
elif r == b and g < r:
    print("fjolubleikur")
elif g == b and r < g:
    print("blagraenn")
elif r==g==b==0:
    print("svartur")
elif r==g==b==255:
    print("hvitur")
elif r == g==b:
    print("grar")
else:
    print("othekkt")