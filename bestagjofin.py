import sys
maximum = -1 * sys.maxsize
n = int(input())
name = ""
for i in range(n):
    nam, m = input().split(" ")
    if int(m) > maximum:
        name = nam
        maximum = int(m)
print(name)