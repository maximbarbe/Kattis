vowels = {"a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"}
res = []
string = input()
for letter in string:
    if letter in vowels:
        res.append(letter)
print("".join(res))