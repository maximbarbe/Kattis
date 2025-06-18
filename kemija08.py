vowels = "aeiou"
string = input()
res = ""
i = 0
while i != len(string):
    if string[i] in vowels:
        res += string[i]
        i += 3
    else:
        res += string[i]
        i += 1
print(res)