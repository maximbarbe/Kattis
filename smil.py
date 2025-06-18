string = input()
indices = []
for i in range(len(string)):
    if string[i] == ":" or string[i] == ";":
        if i + 1 < len(string):
            if string[i + 1] == ")":
                indices.append(i)
        if i + 2 < len(string):
            if string[i + 1] == "-" and string[i + 2] == ")":
                indices.append(i)
for idx in indices:
    print(idx)