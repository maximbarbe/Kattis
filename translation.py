t = int(input())
words = input().split()
translation = dict()
n = int(input())
for i in range(n):
    src, dest = input().split()
    translation[src] = dest
for i in range(len(words)):
    words[i] = translation[words[i]]
print(" ".join(words))