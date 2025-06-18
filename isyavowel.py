vowels = "aeiou"
vowels_occurences = 0
y_occurences = 0
string = input()
for i in range(len(string)):
    if string[i] in vowels:
        vowels_occurences += 1
    elif string[i] == "y":
        y_occurences += 1
print(str(vowels_occurences) + " " + str(vowels_occurences + y_occurences))