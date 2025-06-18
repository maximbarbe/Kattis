stack = []
items = {
    "p": 0,
    "g": 0,
    'o': 0
}
string = input()
for i in range(len(string)):
    if string[i] != '.':
        if string[i] in ["p", "g", "o"]:
            items[string[i]] += 1
            stack.append(string[i])
        else:
            if string[i] == "P":
                if items["p"] == 0:
                    print("Neibb")
                    exit()
                else:
                    while stack[-1] != "p":
                        items[stack.pop()] -= 1
                    items[stack.pop()] -= 1
            elif string[i] == "G":
                if items["g"] == 0:
                    print("Neibb")
                    exit()
                else:
                    while stack[-1] != "g":
                        items[stack.pop()] -= 1
                    items[stack.pop()] -= 1
            else:
                if items["o"] == 0:
                    print("Neibb")
                    exit()
                else:
                    while stack[-1] != "o":
                        items[stack.pop()] -= 1
                    items[stack.pop()] -= 1
print(items["p"])
print(items["g"])
print(items["o"])