from collections import Counter

word = input()
length = len(word)//3
words = [word[0:length], word[length:2*length], word[2*length:]]
count = Counter(words)
for key in count.keys():
    if count[key] > 1:
        print(key)
        exit()