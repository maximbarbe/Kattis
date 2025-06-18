n = int(input())
for i in range(n):
    string = input()
    if string.startswith("Simon says"):
        print(string[10:])