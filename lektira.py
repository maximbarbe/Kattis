import itertools

string = input()
possible_indices = range(1, len(string))

comb = itertools.combinations(possible_indices, 2)
words = []
for i, j in comb:

    words.append(string[0:i][::-1] + string[i:j][::-1] + string[j:][::-1])
words.sort()
print(words[0])