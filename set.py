import itertools

cards_numbers = {}
all_cards = []
num = 1
sets = []
for i in range(4):
    cards = input().split(" ")
    for j in range(3):
        all_cards.append(cards[j])

for i in range(len(all_cards) - 2):
    for j in range(i + 1, len(all_cards) - 1):
        for k in range(j + 1, len(all_cards)):
            for l in range(4):
                if len(set([all_cards[i][l], all_cards[j][l], all_cards[k][l]])) not in [1, 3]:
                    break
            else:
                sets.append(" ".join(map(str, [i + 1, j+1,k+1])))

if len(sets) == 0:
    print("no sets")
else:
    for row in sets:
        print(row)