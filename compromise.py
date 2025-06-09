t = int(input())
for i in range(t):
    zeroes = dict()
    ones = dict()
    n, cols = map(int, input().split(" "))
    for i in range(cols):
        zeroes[i] = 0
        ones[i] = 0
    for j in range(n):
        string = input()
        for k in range(len(string)):
            if string[k] == "0":
                zeroes[k] += 1
            else:
                ones[k] += 1
    for j in range(cols):
        if zeroes[j] > ones[j]:
            print(0, end="")
        else:
            print(1, end="")
    print()