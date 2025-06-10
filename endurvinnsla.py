name = input()
proportion = float(input())
n = int(input())
plastic = 0
non = 0
for i in range(n):
    word = input()
    if word == "plast":
        plastic += 1
    else:
        non += 1
if non / (plastic + non) <= proportion:
    print("Jebb")
else:
    print("Neibb")