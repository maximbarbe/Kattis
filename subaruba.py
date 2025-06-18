command = input()
n = int(input())
vowels = "aeiouy"
if command == "D":
    for i in range(n):
        
        line=input()
        for char in line:
            if char.lower() in vowels:
                print("ub", end="")
            print(char, end="")
        print()
else:
    for j in range(n):
        line = input()
        res = []
        i = 0
        while i != len(line):
            if line[i].lower() != "u":
                res.append(line[i])
                i += 1
            else:
                if i + 2 < len(line):
                    if line[i + 1].lower() == "b" and line[i + 2].lower() in vowels:
                        res.append(line[i + 2])
                        i += 3
                    else:
                        res.append(line[i])
                        i += 1
                else:
                    res.append(line[i])
                    i += 1
        print("".join(res))