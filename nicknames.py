from collections import defaultdict


hashmap = defaultdict(lambda:0)
a = int(input())
for i in range(a):
    s = input()
    for j in range(len(s)):
        hashmap[hash(s[0:j+1])] += 1
    
b = int(input())
for i in range(b):
    print(hashmap[hash(input())])