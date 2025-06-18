conversions = {
    "qwerty": ["~", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/"],
    "dvorak": ["~", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "[", "]", "'", ",", ".", "p", "y","f", "g", "c", "r", "l", "/", "=", "a", "o", "e", "u", "i", "d", "h", "t", "n", "s", "-", ";", "q", "j", "k", "x", "b", "m", "w", "v", "z"],
    "bjarki": ["0", "2", "4", "8", "6", "1", "3", "5", "7", "9", "=", "-", "/", "b", "j", "a", "r", "k", "i", "g", "u", "s", "t", ".", ",", "l", "o", "e", "m", "p", "d", "c", "n", "v", "q", ";", "[", "]", "y", "z", "h", "w", "f", "x", "'", "~"]
}
src, dest = input().split(" on ")
string = input()
res = []
for char in string:
    if char == ' ':
        res.append(' ')
    else:
        res.append(conversions[dest][conversions[src].index(char)])
print("".join(res))