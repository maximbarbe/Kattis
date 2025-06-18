import sys

vowels = "aeiouy"
consonents = "bcdfghjklmnpqrstvwxz"

for line in sys.stdin:
    words = line.rstrip().split(" ")
    converted = []
    for word in words:
        first = word[0]
        if first in vowels:
            converted.append(word + "yay")
        else:
            for i in range(len(word)):
                if word[i] in vowels:
                    converted.append(word[i:] + word[0:i] + "ay")
                    break
    print(" ".join(converted))