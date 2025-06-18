n, m = map(int, input().split())

freq = [[0]*26 for i in range(m)]


c = ord('a')

for i in range(n):
    w = input()
    for j in range(len(w)):
        freq[j][ord(w[j]) - c] += 1

res = ""
for i in range(m):
    letter = 0
    max = 0
    for j in range(26):
        if freq[i][j] > max:
            max = freq[i][j]
            letter = j
    res += chr(c + letter)
print(res)