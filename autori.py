string = input()
result = ""
for i in range(len(string)):
    if string[i].isupper():
        result += string[i]
print(result)