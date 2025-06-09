import sys

first = dict()
find_words = False
for line in sys.stdin:
    if line == "\n":
        find_words = True
        continue
    if find_words:
        line = line.strip("\n")
        if line in first.keys():
            print(first[line])
        else:
            print("eh")
            
    else:
        data = line.strip("\n").split(" ")
        first[data[1]] = data[0]