whitespace = 0
uppercase = 0
lowercase = 0
alpha = 0
string = input()
for i in range(len(string)):
    if string[i]== "_":
        whitespace += 1
    elif string[i].islower():
        lowercase += 1
    elif string[i].isupper():
        uppercase += 1
    else:
        alpha += 1
print(whitespace/len(string))
print(lowercase/len(string))
print(uppercase/len(string))
print(alpha/len(string))