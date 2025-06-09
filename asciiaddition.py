ascii = {
    "0": [
        "xxxxx",
        "x...x",
        "x...x",
        "x...x",
        "x...x",
        "x...x",
        "xxxxx"
        ],
    "1": [
        "....x",
        "....x",
        "....x",
        "....x",
        "....x",
        "....x",
        "....x",
        ],
    "2": [
        "xxxxx",
        "....x",
        "....x",
        "xxxxx",
        "x....",
        "x....",
        "xxxxx"
    ],
    "3": [
        "xxxxx",
        "....x",
        "....x",
        "xxxxx",
        "....x",
        "....x",
        "xxxxx"
    ],
    "4": [
        "x...x",
        "x...x",
        "x...x",
        "xxxxx",
        "....x",
        "....x",
        "....x"
    ],
    "5": [
        "xxxxx",
        "x....",
        "x....",
        "xxxxx",
        "....x",
        "....x",
        "xxxxx"
    ],
    "6": [
        "xxxxx",
        "x....",
        "x....",
        "xxxxx",
        "x...x",
        "x...x",
        "xxxxx"
    ],
    "7": [
        "xxxxx",
        "....x",
        "....x",
        "....x",
        "....x",
        "....x",
        "....x"
    ],
    "8": [
        "xxxxx",
        "x...x",
        "x...x",
        "xxxxx",
        "x...x",
        "x...x",
        "xxxxx"
    ],
    "9": [
        "xxxxx",
        "x...x",
        "x...x",
        "xxxxx",
        "....x",
        "....x",
        "xxxxx"
    ],
    "+": [
        ".....",
        "..x..",
        "..x..",
        "xxxxx",
        "..x..",
        "..x..",
        "....."
    ]
}
expression = ""
ascii_expression = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
for i in range(7):
    ascii_expression[i] = input()
i = 0
while i < len(ascii_expression[0]):
    for key in ascii.keys():
        if ascii_expression[0][i:i+5] == ascii[key][0] and ascii_expression[1][i:i+5] == ascii[key][1] and ascii_expression[2][i:i+5] == ascii[key][2] and ascii_expression[3][i:i+5] == ascii[key][3] and ascii_expression[4][i:i+5] == ascii[key][4] and ascii_expression[5][i:i+5] == ascii[key][5] and ascii_expression[6][i:i+5] == ascii[key][6]:
            expression += key
            break
    
    
    
    i += 6
    
res = str(eval(expression))
res_list = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
for i in range(len(res)):
    for j in range(len(ascii[res[i]])):
        res_list[j].append(ascii[res[i]][j])
for row in res_list:
    print(".".join(row))