letters = {
    "a": "2",
    "b": "22",
    "c": "222",
    "d": "3",
    "e": "33",
    "f": "333",
    "g": "4",
    "h": "44",
    "i": "444",
    "j": "5",
    "k": "55",
    "l": "555",
    "m": "6",
    "n": "66",
    "o": "666",
    "p": "7",
    "q": "77",
    "r": "777",
    "s": "7777",
    "t": "8",
    "u": "88",
    "v": "888",
    "w": "9",
    "x": "99",
    "y": "999",
    "z": "9999",
    " ": "0"
}
n = int(input())
for k in range(n):
    string = input()
    conv = []
    for char in string:
        conv.append(letters[char])
    res = ""
    res += conv[0]
    for i in range(1, len(conv)):
        if conv[i][0] == conv[i - 1][0]:
            res += f" {conv[i]}"
        else:
            res += conv[i]
    print(f"Case #{k + 1}: {res}")