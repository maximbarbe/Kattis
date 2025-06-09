n = int(input())
words = input().split()
count = 1
for i in range(n):
    if words[i].isnumeric() and int(words[i]) != count:
        print("something is fishy")
        exit()
    count += 1
print("makes sense")