from collections import defaultdict
starting_letters = defaultdict(lambda:[])
last_char = input()[-1]
n = int(input())
words = []
for i in range(n):
    word = input()
    starting_letters[word[0]].append(word)
    words.append(word)
res = None
for word in words:
    if word.startswith(last_char):
        if starting_letters[word[-1]] == [] or len(starting_letters[word[-1]]) == 1 and starting_letters[word[-1]][0] == word:
            print(word+"!")
            exit()
        else:
            if res == None:
                res = word
else:
    if res == None:
        print("?")
    else:
        print(res)