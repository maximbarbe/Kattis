n = int(input())
for i in range(n):
    first = input()
    second = input()
    res = ""
    for i in range(len(first)):
        if first[i] == second[i]:
            res += "."
        else:
            res += "*"
    print(first)
    print(second)
    print(res+"\n")