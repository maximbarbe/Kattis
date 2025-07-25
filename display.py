import sys
digits = {
    
    
    "1": [
        "    +",
        "    |",
        "    |",
        "    +",
        "    |",
        "    |",
        "    +"
    ],
    "2": [
        "+---+",
        "    |",
        "    |",
        "+---+",
        "|    ",
        "|    ",
        "+---+"
    ],
    "3": [
        "+---+",
        "    |",
        "    |",
        "+---+",
        "    |",
        "    |",
        "+---+"
    ],
    "4": [
        "+   +",
        "|   |",
        "|   |",
        "+---+",
        "    |",
        "    |",
        "    +"
    ],
    "5": [
        "+---+",
        "|    ",
        "|    ",
        "+---+",
        "    |",
        "    |",
        "+---+"
    ],
    "6": [
        "+---+",
        "|    ",
        "|    ",
        "+---+",
        "|   |",
        "|   |",
        "+---+"
    ],
    "7": [
        "+---+",
        "    |",
        "    |",
        "    +",
        "    |",
        "    |",
        "    +"
    ],
    "8": [
        "+---+",
        "|   |",
        "|   |",
        "+---+",
        "|   |",
        "|   |",
        "+---+"
    ],
    "9": [
        "+---+",
        "|   |",
        "|   |",
        "+---+",
        "    |",
        "    |",
        "+---+"
    ],
    "0": [
        "+---+",
        "|   |",
        "|   |",
        "+   +",
        "|   |",
        "|   |",
        "+---+"
    ],
    ":": [
        " ",
        " ",
        "o",
        " ",
        "o",
        " ",
        " "
    ]
}
for line in sys.stdin:
    line = line.rstrip()
    if line == "end":
        print("end")
        exit()
    res = [
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]
    for char in line:
        for j, line in enumerate(digits[char]):
            res[j].append(line)
    for line in res:
        print("  ".join(line))        
    print()
    print()