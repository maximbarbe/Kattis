from math import floor, sqrt

while True:
    string = input()
    if string == ".":
        break
    div = set()
    for i in range(1, floor(sqrt(len(string))) + 1):
        if len(string) % i == 0:
            div.add(i)
            div.add(len(string) // i)
    div = list(div)
    div.sort()
    for d in div:
        if string[-d:]*(len(string)//d) == string:
            print(len(string)//d)
            break