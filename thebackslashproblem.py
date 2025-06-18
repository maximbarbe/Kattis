import sys

while True:
    try:
        n = int(input())
    except EOFError:
        exit()
    string = input()
    for i in range(n):
        converted = ""
        for j in range(len(string)):
            if ord(string[j]) >= 33 and ord(string[j]) <= 42 or ord(string[j]) >= 91 and ord(string[j]) <= 93:
                converted += f"\\{string[j]}"
            else:
                converted += string[j]
        string = converted
    print(string)