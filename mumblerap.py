length = int(input())
string = input()
res = 0
i = 0
while i < len(string):
    if string[i].isnumeric():
        cur = string[i]
        j = i + 1
        while j < len(string) and string[j].isnumeric():
            cur += string[j]
            j += 1
        if int(cur) > res:
            res = int(cur)
        i = j
    i += 1
print(res)