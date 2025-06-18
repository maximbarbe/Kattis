src = input()
dest = input()
i = 0
for j in range(len(dest)):
    if i == len(src):
        print("Ja")
        exit()
    else:
        if dest[j] == src[i]:
            i += 1
else:
    if i == len(src):
        print("Ja")
    else:
        print("Nej")