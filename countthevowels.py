vowels = ["a", "e", "i", "o", "u"]
string = input().lower()
res = 0
for i in range(len(string)):
    if string[i] in vowels:
        res += 1
print(res)