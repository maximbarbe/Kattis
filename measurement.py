factor = {
    "thou": 1,
    "inch": 1000,
    "foot": 12000,
    "yard": 36000,
    "chain": 792000,
    "furlong": 7920000,
    "mile": 63360000,
    "league": 190080000
}
acronyms = {
    "th": "thou",
    "in": "inch",
    "ft": "foot",
    "yd": "yard",
    "ch": "chain",
    'fur': "furlong",
    "mi": "mile",
    "lea": "league"
}
data = input().split(" ")
quant = int(data[0])
src = data[1] if data[1] in factor.keys() else acronyms[data[1]]
dest = data[3] if data[3] in factor.keys() else acronyms[data[3]]

print(quant * factor[src]/factor[dest])