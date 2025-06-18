name = input()
a = int(input())
b = int(input())
c = int(input())
if a - b == c and abs(a-b) != c:
    print("JEDI")
elif a - b != c and abs(a-b) == c:
    print("SITH")
else:
    print("VEIT EKKI")