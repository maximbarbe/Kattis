g,s,c = map(int, input().split())

buy = 3 * g + 2*s+c
vic = None
treasure = None
if buy >= 8:
    vic = "Province"
    treasure = "Gold"
elif buy >= 6:
    vic = "Duchy"
    treasure = "Gold"
elif buy >= 5:
    vic = "Duchy"
    treasure = "Silver"
elif buy >= 3:
    vic = "Estate"
    treasure = "Silver"
elif buy >= 2:
    vic = "Estate"
    treasure = "Copper"
else:
    treasure = "Copper"

if not vic:
    print(treasure)
else:
    print(f"{vic} or {treasure}")