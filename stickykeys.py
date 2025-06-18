string = input()
res = ""
i = 0
while i != len(string):
    res += string[i]
    j = i + 1
    while j < len(string) and string[j] == string[i]:
        j += 1
    i = j
print(res)