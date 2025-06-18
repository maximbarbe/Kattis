n = input()

x = 0
y = 0
for i in range(len(n)-1, -1, -1):
    if n[i] == "0":
        continue
    elif n[i] == "1":
        x += 2 **(len(n) - i - 1)
    elif n[i] == "2":
        y += 2 ** (len(n) - i - 1)
    else:
        x += 2 ** (len(n) - i - 1)
        y += 2 ** (len(n)  - i - 1)

print(len(n), x, y)