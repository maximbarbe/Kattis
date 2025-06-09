from string import ascii_uppercase
from functools import cmp_to_key



def cmp(s1:str, s2:str):
    i1 = 0
    i2 = 0
    for i in range(len(s1)):
        if s1[i].isupper():
            i1 = i
            break
    for i in range(len(s2)):
        if s2[i].isupper():
            i2 = i
            break
        
    while i1 != len(s1) and i2 != len(s2):
        if s1[i1] < s2[i2]:
            return -1
        elif s1[i1] > s2[i2]:
            return 1
        i1 += 1
        i2 += 1
    if i1 == len(s1) and i2 == len(s2):
        return 0
    elif i1 == len(s1):
        return -1
    else:
        return 1
    
n = int(input())
strings = []
for i in range(n):
    strings.append(input())
strings.sort(key=cmp_to_key(cmp))
for s in strings:
    print(s)