n = int(input())
words = input().split(" ")
res =""
for word in words:
    if word[0].isupper():
        res += word[0]
print(res)