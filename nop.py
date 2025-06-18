res= 0
string = input()
for i in range(len(string)):
    if string[i].isupper():
        if (i + res) % 4 != 0:
            while (i + res) % 4 != 0:
                res += 1
print(res)