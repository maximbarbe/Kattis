diff = int(input())
string = [*input()]
count = {
    "M" : 0,
    "W" : 0
}
res = 0
for i in range(len(string) - 1):
    count[string[i]] += 1
    if abs(count["M"] - count["W"]) <= diff:
        continue
    else:
        count[string[i]] -= 1
        string[i], string[i + 1] = string[i + 1], string[i]
        count[string[i]] += 1
        if abs(count["M"] - count["W"]) > diff:
            count[string[i]] -= 1
            break
else:
    count[string[-1]] += 1
    if abs(count["M"] - count["W"]) > diff:
        count[string[-1]] -= 1
print(count["M"] + count["W"])