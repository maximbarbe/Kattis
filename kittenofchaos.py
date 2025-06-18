letters = [char for char in input()]
transformations = input()
h = False
v = False
r = False
for _ in transformations:
    if _ == "h":
        h ^= 1
    elif _ == "v":
        v ^= 1
    else:
        r ^= 1
if h:
    for i, char in enumerate(letters):
        match char:
            case "b":
                letters[i] = "d"
            case "d":
                letters[i] = "b"
            case "p":
                letters[i] = "q"
            case "q":
                letters[i] = "p"
    letters = letters[::-1]
if v:
    for i, char in enumerate(letters):
        match char:
            case "b":
                letters[i] = "p"
            case "d":
                letters[i] = "q"
            case "p":
                letters[i] = "b"
            case "q":
                letters[i] = "d"
if r:
    for i, char in enumerate(letters):
        match char:
            case "b":
                letters[i] = "q"
            case "d":
                letters[i] = "p"
            case "p":
                letters[i] = "d"
            case "q":
                letters[i] = "b"
    letters = letters[::-1]
print("".join(letters))