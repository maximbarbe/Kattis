power_levels = {
    "Shadow": 6,
    "Gale": 5,
    "Ranger": 4,
    "Anvil": 7,
    "Vexia": 3,
    "Guardian": 8,
    "Thunderheart": 6,
    "Frostwhisper": 2,
    "Voidclaw": 3,
    "Ironwood": 3,
    "Zenith": 4,
    "Seraphina": 1
}
total1 = 0
total2 = 0
wins1 = 0
wins2 = 0
ties = 0
for i in range(3):
    n1, *data1 = input().split()
    p1 = 0
    n2, *data2 = input().split()
    p2 = 0
    for _ in data1:
        if _ == "Zenith" and i == 1:
            p1 += power_levels[_] + 5
        elif _ == "Thunderheart" and n1 == "4":
            p1 += 2 * power_levels[_]
        elif _ == "Seraphina":
            p1 += int(n1)
        else:
            p1 += power_levels[_]
    for _ in data2:
        if _ == "Zenith" and i == 1:
            p2 += power_levels[_] + 5
        elif _ == "Thunderheart" and n2 == "4":
            p2 += 2 * power_levels[_]
        elif _ == "Seraphina":
            p2 += int(n2)
        else:
            p2 += power_levels[_]
    total1 += p1
    total2 += p2
    if p1 > p2:
        wins1 += 1
    elif p2 > p1:
        wins2 += 1
    else:
        ties += 1
if ties == 3:
    print("Tie")
elif wins1 > wins2:
    print('Player 1')
elif wins2 > wins1:
    print('Player 2')
else:
    if total1 > total2:
        print('Player 1')
    elif total2 > total1:
        print('Player 2')
    else:
        print('Tie')