from collections import defaultdict
word = input()
hangman = [False for i in range(len(word))]
indices = defaultdict(lambda:[])
for i in range(len(word)):
    indices[word[i]].append(i)
fails = 0
alphabet = input()
for i in range(len(alphabet)):
    if False not in hangman:
        print("Win")
        exit()
    if fails >= 10:
        print("LOSE")
        exit()
    if indices[alphabet[i]] == []:
        fails += 1
    else:
        for idx in indices[alphabet[i]]:
            hangman[idx] = True
if False not in hangman:
    print("WIN")
    exit()
if fails >= 10:
    print("LOSE")
    exit()