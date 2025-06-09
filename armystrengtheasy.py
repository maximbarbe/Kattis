n = int(input())
for i in range(n):
    input()
    ng, nm = map(int, input().split(" "))
    godzilla = [*map(int, input().split(" "))]
    mecha = [*map(int, input().split(" "))]
    godzilla.sort()
    mecha.sort()
    while godzilla != [] and mecha != []:
        if godzilla[0] < mecha[0]:
            godzilla.pop(0)
        elif godzilla[0] >= mecha[0]:
            mecha.pop(0)
    if godzilla == []:
        print("MechaGodzilla")
    else:
        print("Godzilla")