n = int(input())
s1 = input()
s2 = input()
res = 0
for a, b in zip(s1, s2):
    
    res += min((ord(a) - ord('A') - (ord(b) - ord('A')))%26, (ord(b) - ord('A') - (ord(a) - ord('A')))%26)
print(res)