n = int(input())
names = []
idx = 0
for i in range(n):
    names.append(input())
for i in range(len(names)):
    if (i + 12)%len(names) == 0:
        idx = i
        break
for i in range(idx, len(names) + idx):
    print(names[i % len(names)])