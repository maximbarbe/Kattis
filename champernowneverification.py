string = input()
i = 0
num = 1
while i < len(string):
    if i + len(str(num)) > len(string):
        print(-1)
        exit()
    if str(num) != string[i:i+len(str(num))]:
        print(-1)
        exit()
    i += len(str(num))
    num += 1
print(str(num - 1))