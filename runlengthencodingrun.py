type, string = input().split(" ")
if type == "D":
    res = ""
    for i in range(0, len(string), 2):
        char = string[i]
        freq = int(string[i + 1])
        res += char * freq
    print(res)
else:
    res = ""
    i = 0
    while i < len(string):
        j = i + 1
        while j < len(string) and string[j] == string[i]:
            j += 1
        res += f"{string[i]}{j - i}"
        i = j
    print(res)
        