from collections import defaultdict
n = int(input())
names = defaultdict(lambda:0)
for i in range(n):
    name = input()
    names[name] = 0
n = int(input())
for i in range(n):
    data = input().split(" ")
    if data[0] == "0":
        continue
    students = data[1:]
    for student in students:
        names[student] += 1
for key in sorted(names.keys(), key = lambda x: names[x], reverse = True):
    print(f"{names[key]} {key}")