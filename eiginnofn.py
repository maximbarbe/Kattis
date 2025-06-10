from collections import defaultdict

at_home = defaultdict(lambda:False)
other_name = defaultdict(lambda:None)
n = int(input())
for i in range(n):
    data = input().split(" ")
    at_home[data[0]] = True
    if len(data) == 2:
        other_name[data[0]] = data[1]
        
n = int(input())
for i in range(n):
    name = input()
    if at_home[name] == False:
        print("Neibb")
    else:
        if other_name[name] != None:
            print(f"Neibb en {name} {other_name[name]} er heima")
        else:
            print("Jebb")