string = input()
res = []
i = 0

converted = {
    "R": "S",
    "B": "K",
    "L": "H"
}

while i != len(string):
    if i + 2 < len(string):
        if string[i] != string[i+1] and string[i + 1] != string[i + 2] and string[i] != string[i +2]:
            res.append("C")
            i += 3
        else:
            res.append(converted[string[i]])
            i += 1
    else:
        res.append(converted[string[i]])
        i += 1
print("".join(res))