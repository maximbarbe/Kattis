from string import punctuation
s = input()
s = s.split()
cur = []
res = []
for word in s:
    for char in punctuation:
        word = word.replace(char, "")
    t = set(word)

    if (len(t) == 2 and "u" in t and "m" in t) or (len(t) == 1 and ("m" in t or "u" in t)):
        for char in word:
            if char == "u":
                cur.append("1")
            elif char == "m":
                cur.append("0")
            if len(cur) == 7:
                res.append(chr(int("".join(cur), 2)))
                cur = []
print("".join(res))