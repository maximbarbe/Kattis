from collections import defaultdict

base = int(input())

chars = input().split(" ")
mapping = dict()
for i in range(len(chars)):
    mapping[chars[i]] = i
    
digits = []
string = input()
cur= ""
for i in range(len(string)):
    cur += string[i]
    if cur in mapping.keys():
        digits.append(mapping[cur])
        cur = ""
        
res = 0
for i in range(len(digits)):
    res += digits[i] * pow(base, len(digits) - 1 - i)
print(res)