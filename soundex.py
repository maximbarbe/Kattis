import sys

mapping = {
    "B": "1",
    "F": "1",
    "P": "1",
    "V": "1",
    "C": "2",
    "G": "2",
    "J": "2",
    "K": "2",
    "Q": "2",
    "S": "2",
    "X": "2",
    "Z": "2",
    "D": "3",
    "T": "3",
    "L": "4",
    "M": "5",
    "N": "5",
    "R": "6"
    }
for line in sys.stdin:
    code =""
    prev = None
    for char in line.rstrip():
        converted = mapping.get(char, "")
        if converted != prev:
            code += converted
            prev = converted
    print(code)