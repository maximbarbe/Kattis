from collections import defaultdict
n, m = map(int, input().split(" "))
dict = defaultdict(lambda:[])
for i in range(n):
    name = input()
    names = name.split(" ")
    dict[f"{names[0][0]}{names[1][0]}"].append(name)
for i in range(m):
    initials = input()
    if len(dict[initials]) ==  0:
        print("nobody")
    elif len(dict[initials]) == 1:
        print(dict[initials][0])
    else:
        print("ambiguous")