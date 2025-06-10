import sys
words = []
for i in range(2):
    string = input().split("|")
    words += string
print(f"{words[0]}{words[2]} {words[1]}{words[3]}")