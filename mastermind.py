from collections import Counter

data = input().split()
n = int(data[0])
code, guess = data[1], data[2]

c1 = Counter([char for char in code])
c2 = Counter([char for char in guess])
r = s = 0
for i in range(n):
    if code[i] == guess[i]:
        r += 1
        c1[code[i]] -= 1
        c2[code[i]] -= 1
for letter in c2.keys():
    s += min(c1[letter], c2[letter])
print(r, s)