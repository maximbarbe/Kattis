p, n = map(int, input().split(" "))
parts = set()
for i in range(1, n+1):
    string = input()
    parts.add(string)
    if len(parts) == p:
        print(i)
        exit()
else:
    print("paradox avoided")