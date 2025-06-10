import sys

conversions = {
    'A': ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "_": "..--",
    ",": ".-.-",
    ".": "---.",
    "?": "----"
}
reverse = {val:key for key, val in conversions.items()}
for line in sys.stdin:
    line = line.strip("\n")
    lengths = []
    morse = []
    for i in range(len(line)):
        morse.append(conversions[line[i]])
        lengths.append(len(conversions[line[i]]))
    lengths.reverse()
    morse = "".join(morse)
    i = 0
    lengths_idx = 0
    res = str()
    while lengths_idx != len(lengths):
        res += reverse[morse[i:i+lengths[lengths_idx]]]
        i += lengths[lengths_idx]
        lengths_idx += 1
    print(res)