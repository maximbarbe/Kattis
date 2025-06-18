def backtrack(chars, pairs, idx):
    global res
    for i in range(idx, len(pairs)):
        j, k = pairs[i]
        chars[j] = ""
        chars[k] = ""
        backtrack(chars, pairs, i + 1)
        chars[j] = "("
        chars[k] = ")"
    else:
        res.add("".join(chars))
string = input()
stack = []
pairs = []
res = set()
for i in range(len(string)):
    if string[i] == "(":
        stack.append(i)
    elif string[i] == ")":
        pairs.append((stack.pop(), i))


backtrack([*string], pairs, 0)
res.remove(string)
res = sorted(res)
for _ in res:
    print(_)