string = input()
res = 0
for i in range(len(string)):
    if string[i].isalpha():
        res += 1
    
print(res)