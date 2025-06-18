from collections import Counter
word=input()
guess = input()
letters = Counter([char for char in word])
res = ["-"]*len(word)

for i in range(len(res)):
    if guess[i] == word[i]:
        res[i] = "G"
        letters[guess[i]] -= 1
for i in range(len(res)):
    if guess[i] != word[i] and letters[guess[i]] != 0:
        res[i] = "Y"
        letters[guess[i]] -= 1
print("".join(res))