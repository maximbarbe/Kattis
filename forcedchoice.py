n, p , s = map(int, input().split())
for i in range(s):
    cards = [*map(int, input().split())]
    if p in cards[1:]:
        print("KEEP")
    else:
        print("REMOVE")