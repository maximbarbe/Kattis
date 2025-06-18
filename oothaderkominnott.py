i = int(input())
if i == 1:
    l = w = int(input())
    res = 2*l*3 + 2*(l-2)*3 + (l-2)**2
    print(res)
elif i == 2:
    l = int(input())
    w = int(input())
    res = 2*l*3 + 2*(w-2)*3 + (w-2)*(l-2)
    print(res)
else:
    l = int(input())
    w = int(input())
    h = int(input())
    res = 2*l*h + 2*(w-2)*h + (w-2)*(l-2)
    print(res)