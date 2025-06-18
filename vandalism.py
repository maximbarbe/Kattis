s = input()
res = ""
for char in "UAPC":
    if char not in s:
        res += char
print(res)