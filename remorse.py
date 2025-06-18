from collections import Counter

encodings = [".", "._.", "-", "._._.", "._-", "-_.", "._._._.", "-_._.", "._-_.", "._._-", "-_-", "._._._._.", "-_._._.", "._-_._.", "._._-_.", "._._._-", '._-_-', '-_._-', "-_-_.", "._._-_-", "._-_._-", "._-_-_.", "-_._._-", "-_._-_.", "-_-_._.", "-_-_-"]
string = input()
parsed = ""
for char in string:
    if char.isalpha():
        parsed += char
c = Counter()
res = (len(parsed) - 1) * 3
for char in parsed:
    if char.isalpha():
        c[char.upper()] += 1
for i, val in enumerate(sorted(c.values(), reverse=True)):
    cur = 0
    for char in encodings[i]:
        match char:
            case ".":
                cur += 1
            case "_":
                cur += 1
            case _:
                cur += 3
    res += cur * val
print(res)