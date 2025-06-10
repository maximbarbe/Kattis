res = 1
first = input()
second = input()
for i in range(4):
    if first[i] != second[i]:
        res *= 2
print(res)