from math import inf

string = input()
sequences = [[string[i]] for i in range(len(string))]
max_length = 1
for i in range(len(sequences) -2, -1, -1):
    for j in range(i + 1, len(sequences)):
      if string[i] < string[j] and len(sequences[i]) - 1 < len(sequences[j]):
          sequences[i] = [string[i]] + sequences[j]
    if len(sequences[i]) > max_length:
        max_length = len(sequences[i])

print(26 - max_length)