n = int(input())
string = input()
res = 0
cups = 0
for char in string:
    if char == "1":
        res += 1
        cups = 2
    else:
        if cups != 0:
            res += 1
            cups -= 1
print(res)