string = input()
cards = {
    "P": set(),
    "K": set(),
    "H": set(),
    "T": set()
}
for i in range(len(string)//3):
    card = string[3*i:3*i+3]
    if int(card[1:]) in cards[card[0]]:
        print("GRESKA")
        exit()
    else:
        cards[card[0]].add(int(card[1:]))
print(f"{13 - len(cards['P'])} {13 - len(cards['K'])} {13 - len(cards['H'])} {13 - len(cards['T'])}")