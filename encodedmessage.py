from math import sqrt
n = int(input())
for i in range(n):
    string = input()
    side = int(sqrt(len(string)))
    offset = side - 1
    decoded = ""
    while offset != -1:
        cur = offset
        while cur < len(string):
            decoded += string[cur]
            cur += side
        offset -= 1
    print(decoded)