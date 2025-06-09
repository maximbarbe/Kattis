word = input()
num_days = len(word)
for i in range(len(word)):
    if word[i] == "P" and i % 3 == 0:
        num_days -= 1
    elif word[i] == "E" and i % 3 == 1:
        num_days -= 1
    elif word[i] == "R" and i % 3 == 2:
        num_days -= 1
print(num_days)