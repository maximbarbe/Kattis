res = 0
left = 0

string = input()
for i in range(len(string)):
    if string[i] == ">":
        left += 1
    elif string[i] == "<":
        res += left
print(res)