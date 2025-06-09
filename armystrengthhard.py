n = int(input())
for i in range(n):
    input()
    ng, nm = map(int, input().split(" "))
    godzilla = [*map(int, input().split(" "))]
    mecha = [*map(int, input().split(" "))]
    godzilla.sort()
    mecha.sort()
    i = 0
    j = 0
    while i != len(godzilla) and j != len(mecha):
        if godzilla[i] < mecha[j]:
            i += 1
        else:
            j += 1
    if i == len(godzilla):
        print("MechaGodzilla")
    else:
        print("Godzilla")