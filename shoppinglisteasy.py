from collections import Counter

words = []
n, m = map(int, input().split(" "))
for i in range(n):
    words.extend(input().split(" "))
freq = Counter(words)
res = []
for key in freq.keys():
    if freq[key] == n:
        res.append(key)
res.sort()
print(len(res))
for word in res:
    print(word)