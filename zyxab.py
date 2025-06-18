n = int(input())
names = []
for i in range(n):
    name = input()
    if len(name) < 5 or len(set(name)) != len(name):
        continue
    else:
        names.append(name)
if len(names) == 0:
    print("Neibb")
else:
    names.sort(key = lambda el: (-len(el), el), reverse=True)
    print(names[0])
