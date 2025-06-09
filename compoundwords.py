from sys import stdin

words = []

combinations = set()
temp = list(stdin)
for string in temp:
    sep = string.rstrip("\n").split(" ")
    words += sep

if len(words) == 1:
    print(words[0])
    exit()
for i in range(len(words)):
    for j in range(len(words)):
        if i != j:
            combinations.add(words[i] + words[j])
combinations = list(sorted(combinations))
for word in combinations:
    print(word)