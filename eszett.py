response = []
def res(string, cur, idx):
    if idx == len(string):
        response.append(cur)
        return
    else:
        if string[idx] == "S" and idx + 1 != len(string) and string[idx + 1] == "S":
            res(string, cur + "B", idx + 2)
            res(string, cur + "S", idx + 1)
            return
        else:
            res(string, cur + string[idx], idx + 1)
            return
s = input()
res(s, "", 0)
response = list(set(response))
for el in response:
    print(el)