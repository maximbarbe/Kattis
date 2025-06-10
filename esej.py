import random
alphabet = "abcdefghijklmnopqrstuvwxyz"
a, b = map(int, input().split(" "))
words = []
for i in range(b):
    string = ""
    for j in range(14):
        string += random.choice(alphabet)
    words.append(string)
print(" ".join(words))