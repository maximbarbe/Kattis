from collections import defaultdict
import sys
dict = defaultdict(lambda: 0)
n = int(input())
for i in range(n):
    name, f = input().split(" ")
    dict[name] += int(f)
    
maximum = -1 * sys.maxsize
name = ""
for key, val in dict.items():
    if val > maximum:
        maximum = val
        name = key
print(name)