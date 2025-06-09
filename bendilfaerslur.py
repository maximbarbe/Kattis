string = input()
if "." in string:
    string = string.split(".")[::-1]
    print(".".join(string) + ".in-addr.arpa.")
else:
    if string.startswith("::"):
        string = string.split(":")[2:]
        chars = []
        for char in string:
            for j in range(4 - len(char)):
                chars.append("0")
            for c in char:
                chars.append(c)
        chars = chars[::-1] + ["0"] * (32 - len(chars))
        print(".".join(chars) + ".ip6.arpa.")
    elif string.endswith("::"):
        string = string.split(":")[:-2]
        chars = []
        for char in string:
            for j in range(4 - len(char)):
                chars.append("0")
            for c in char:
                chars.append(c)
        chars = ["0"] * (32 - len(chars)) + chars[::-1]
        print(".".join(chars) + ".ip6.arpa.")
    else:
        string = string.split(":")
        left = []
        right = []
        t = False
        for i in range(len(string)):
            if string[i] == "":
                t = True
            else:
                if not t:
                    for j in range(4 - len(string[i])):
                        left.append("0")
                    for c in string[i]:
                        left.append(c)
                else:
                    for j in range(4 - len(string[i])):
                        right.append("0")
                    for c in string[i]:
                        right.append(c)
        left = left[::-1]
        right = right[::-1]
        res = right + ["0"]*(32-len(left)-len(right)) + left
        
        print(".".join(res)+".ip6.arpa.")