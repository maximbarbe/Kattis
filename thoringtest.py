n = int(input())
words = set()
for i in range(n):
    words.add(input().lower())
line = input().split()
for word in map(lambda el: el.lower(), line):
    if word not in words:
        print("Thore has left the chat")
        exit()
print("Hi, how do I look today?")
