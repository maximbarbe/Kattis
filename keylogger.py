caps = False
shift = False
res = []

convert = {
    "clank": "a",
    "bong": "b",
    "click": "c",
    "tap": "d",
    "poing": "e",
    "clonk": "f",
    "clack": "g",
    "ping": "h",
    "tip": "i",
    "cloing": "j",
    "tic": "k",
    "cling": "l",
    "bing": "m",
    "pong": "n",
    "clang": "o",
    "pang": "p",
    "clong": "q",
    "tac": "r",
    'boing': "s",
    "boink": "t",
    "cloink": "u",
    "rattle": "v",
    "clock": "w",
    "toc": "x",
    "clink": "y",
    "tuc": "z",
    "whack": " ",

    
}
n = int(input())
for i in range(n):
    sound = input()
    if sound == "pop":
        if len(res) != 0:
            res.pop()
    else:
        if sound == "bump":
            caps ^= True
        elif sound == "dink":
            shift = True
        elif sound == "thumb":
            shift = False
        else:
            res.append(convert[sound].upper() if shift^caps == True else convert[sound])
print("".join(res))