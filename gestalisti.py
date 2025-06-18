from collections import defaultdict

n = int(input())

guests = defaultdict(lambda:False)
for i in range(n):
    sign, name = input().split()
    match sign:
        case "+":
            guests[name] = True
        case "-":
            guests[name] = False
        case "?":
            print(("Neibb","Jebb")[guests[name]==True])