letters = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "j",
    10: "k",
    11: "l",
    12: 'm',
    13: "n",
    14: "o",
    15: "p",
    16: "q",
    17: "r",
    18: "s",
    19: "t",
    20: "u",
    21: "v",
    22: "w",
    23: "x",
    24: "y",
    25: "z"
}
inverse = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k":10,
    "l":  11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x":  23,
    "y": 24,
    "z": 25
}
n, m = map(int, input().split(" "))
first = input()
encrypted = input()
decoded = [None for i in range(len(encrypted) - n)] + [char for char in first]
keys = [None for i in range(len(encrypted))]
for i in range(len(encrypted) - 1, len(encrypted) - 1 - n, -1):

    keys[i] = (inverse[encrypted[i]] - inverse[first[-1 * (len(encrypted) - i)]] + 26)%26
cur = len(encrypted) - 1
cur_letter = cur - n
while (cur_letter >= 0):
    decoded[cur_letter] = letters[keys[cur]]
    keys[cur_letter]  = (inverse[encrypted[cur_letter]] - inverse[decoded[cur_letter]] + 26)%26
    cur_letter -= 1
    cur -= 1
print("".join(decoded))