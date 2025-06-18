first = input()
second = input()
res = 1
for i in range(len(first)):
    if first[i] != second[i]:
        res += 1
print(res)