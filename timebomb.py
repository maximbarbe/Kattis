reps = [
    [
        "***",
        "* *",
        "* *",
        "* *",
        "***"
    ],
    [
        "  *",
        "  *",
        "  *",
        "  *",
        "  *"
    ],
    [
        "***",
        "  *",
        "***",
        "*  ",
        "***"
        
    ],
    [
        "***",
        "  *",
        "***",
        "  *",
        "***"
    ],
    [
        "* *",
        "* *",
        "***",
        "  *",
        "  *"
    ],
    [
        "***",
        "*  ",
        "***",
        "  *",
        "***"
        
    ],
    [
        "***",
        "*  ",
        "***",
        "* *",
        "***"
    ],
    [
        "***",
        "  *",
        "  *",
        "  *",
        "  *"
    ],
    [
        "***",
        "* *",
        "***",
        "* *",
        "***"
    ],
    [
        "***",
        "* *",
        "***",
        "  *",
        "***"
    ]
    
]
rows = []
numbers = []
for i in range(5):
    rows.append(input())
for i in range(0, len(rows[0]) - 2, 4):
    cur = []
    for j in range(len(rows)):
        cur.append(rows[j][i:i+3])
    numbers.append(cur)
res = []
for i in range(len(numbers)):
    if numbers[i] not in reps:
        print("BOOM!!")
        exit()
    else:
        res.append(reps.index(numbers[i]))
converted = 0
for i in range(len(res)):
    converted += res[i] * 10**(len(res) - 1 - i)
if converted % 6 == 0:
    print("BEER!!")
else:
    print("BOOM!!")