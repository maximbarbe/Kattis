chars = input()
string = input().split(" ")
mappingchars = dict()
mappingstrings = dict()
if len(chars) != len(string):
    print("False")
    exit()
for i in range(len(chars)):
    if (mappingchars.get(chars[i], False) and mappingchars[chars[i]] != string[i]) or (mappingstrings.get(string[i], False)) and mappingstrings[string[i]] != chars[i]:
        print("False")
        exit()
    mappingchars[chars[i]] = string[i]
    mappingstrings[string[i]] = chars[i]
print("True")