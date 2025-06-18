n = int(input())
for i in range(n):
    string = input()
    if string.startswith("simon says "):
        print(string[11:])
    else:
        print()