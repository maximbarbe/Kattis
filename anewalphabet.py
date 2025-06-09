conversion = {
    "a": "@",
    "b": "8",
    "c": "(",
    "d": "|)",
    "e": "3",
    "f": "#",
    "g": "6",
    "h": "[-]",
    "i": "|",
    "j": "_|",
    "k": "|<",
    "l": "1",
    "m": "[]\/[]",
    "n": "[]\[]",
    "o": "0",
    "p": "|D",
    "q": "(,)",
    "r": "|Z",
    "s": "$",
    "t": "']['",
    "u": "|_|",
    "v": "\/",
    "w": "\/\/",
    "x": "}{",
    "y":  "`/",
    "z": "2"
}

string = input().lower()
converted = ""
for char in string:
    if char not in conversion.keys():
        converted += char
    else:
        converted += conversion[char]
print(converted) 