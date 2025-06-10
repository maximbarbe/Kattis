import sys
words = []
for line in sys.stdin:
    line = line.rstrip()
    if line == "":
        words.sort()
        max_length = len(max(words, key=len))
        for word in words:
            print(" "*(max_length - len(word)) + word[::-1])
        words = []
        print()
    else:
        words.append(line[::-1])
else:
    words.sort()
    max_length = len(max(words, key=len))
    for word in words:
        print(" "*(max_length - len(word)) + word[::-1])
    