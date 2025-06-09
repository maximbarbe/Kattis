n = int(input())
for i in range(n):
    m = int(input())
    blue = []
    red = []
    chosen = []
    res = 0
    ropes = input().split(" ")
    for j in range(m):
        if ropes[j][-1] == "B":
            blue.append(int(ropes[j][:-1]))
        else:
            red.append(int(ropes[j][:-1]))
    blue.sort(reverse=True)
    red.sort(reverse=True)
    while blue != [] and red != []:
        chosen.append(blue.pop(0))
        chosen.append(red.pop(0))
    res += sum(chosen)
    res -= (len(chosen))
    print(f"Case #{i+1}: {res}")