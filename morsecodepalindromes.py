convert = {
    "A": ".-",
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
    "T":"-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y" : "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}

converted = ""
string = input()
for char in string:
    converted += convert.get(char.upper(), "")
    
start, end = 0, len(converted) - 1
if len(converted) == 0:
    print(0)
    exit()
while start < end:
    if converted[start] != converted[end]:
        print(0)
        exit()
    start += 1
    end -= 1
else:
    print(1)