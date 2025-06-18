from math import floor

n = int(input())
words = []

for i in range(n):
    words.append(input())
    
res = ""

for i in range(len(max(words, key=len))):
    cur = 0
    sumn = 0
    for j in range(len(words)):
        if i < len(words[j]):
            cur += 1
            sumn += ord(words[j][i]) - ord("a")
    res += chr(ord("a") + floor(sumn/cur))
print(res)