n1, n2 = map(int, input().split())
first = input()
second = input()
ants = []
for i in range(len(first) -1,-1,-1):
    ants.append((first[i], "R"))
for i in range(len(second)):
    ants.append((second[i], "L"))
t = int(input())
for i in range(t):
    j = 0
    while j <  len(ants):
        if j == len(ants) - 1:
            break
        if ants[j][1] == "R" and ants[j+1][1] == "L":
            ants[j], ants[j + 1] = ants[j + 1], ants[j]
            j += 2
        else:
            j += 1
for i in range(len(ants)):
    print(ants[i][0], end="")
print()