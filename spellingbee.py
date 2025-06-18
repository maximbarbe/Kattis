hexword = input()
n = int(input())
for i in range(n):
    word = input()
    if len(word) < 4:
        continue
    if hexword[0] not in word:
        continue
    for letter in word:
        if letter not in hexword:
            break
    else:
        print(word)