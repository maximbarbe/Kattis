t = int(input())
for i in range(t):
    original = set(input())
    abb = set(input())
    if len(original.intersection(abb)) == len(abb):
        print("YES")
    else:
        print("NO")