words = set()
n = int(input())
for i in range(n):
    words.add(input().replace("-", " ").lower())
print(len(words))