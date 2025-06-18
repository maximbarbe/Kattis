pattern = input()
n = int(input())
words = input().split()
w = len(pattern)
res = 0
for word in words:
    for i in range(len(word) - w+1):
        if word[i:i+w] == pattern:
            res += 1
print(res)