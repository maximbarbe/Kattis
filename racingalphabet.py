from math import pi

circ = 2 * pi * 30
dist = circ/28
pos = {
    "A": 0,
    "B": 1,
    "C": 2, 
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
    " ": 26,
    "'": 27
}
n = int(input())
for i in range(n):
    
    string = input()
    res = len(string)
    cur = pos[string[0]]
    for char in string[1:]:
        minimum = min((cur - pos[char] + 28) % 28, (pos[char] - cur + 28)  % 28)
        res += (minimum)  * dist/15
        cur = pos[char]
    print(res)