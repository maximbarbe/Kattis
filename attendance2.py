n = int(input())
words = []
for i in range(n):
    words.append(input())
    
names = []

for i in range(n - 1):
    if words[i] != "Present!":
        if words[i +1] != "Present!":
            names.append(words[i])
if words[-1] != "Present!":
    names.append(words[-1])
if len(names) == 0:
    print("No Absences")
else:
    for name in names:
        print(name)