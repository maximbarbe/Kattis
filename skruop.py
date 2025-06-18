n = int(input())
res = 7
for i in range(n):
    string = input()
    if string == "Skru op!":
        if res < 10:
            res += 1
    else:
        if res > 0:
            res -= 1
print(res)