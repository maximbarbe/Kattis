string = input()
res = ""
i = 0
while i < len(string):
    j = i + 1
    while j < len(string) and string[j] == string[i]:
        j += 1
    res += string[i]
    i = j
print(res)