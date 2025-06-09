word = " "
for char in input():
    if char != word[-1]:
        word += char
print(word.lstrip())