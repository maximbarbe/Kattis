i1 = input()
i2 = input()
n1 = [*map(int, i1.split("."))]
n2 = [*map(int, i2.split("."))]
if n1[0] > n2[0]:
    print(i1)
elif n2[0] > n1[0]:
    print(i2)
else:
    if i1 == i2:
        print(i1)
    elif n1[1] == n2[1]:
        print(-1)
    else:
        i1 = float(i1)
        i2 = float(i2)
        if n1[1] > n2[1]:
            if i1 > i2:
                print(i1)
            else:
                print(-1)
        else:
            if i1 < i2:
                print(i2)
            else:
                print(-1)