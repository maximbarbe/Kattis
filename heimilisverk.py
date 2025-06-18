s = set()
for i in range(int(input())):
    v=input()
    if v not in s:
        print(v)
        s.add(v)