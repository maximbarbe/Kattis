dominant = {
    "A": 11,
    "K": 4,
    "Q": 3,
    "J": 20,
    "T": 10,
    "9": 14,
    "8": 0,
    "7": 0
}
non_dominant = {
    "A": 11,
    "K": 4,
    "Q": 3,
    "J": 2,
    "T": 10,
    "9": 0,
    "8": 0,
    "7": 0
}
data = input().split(" ")
n = int(data[0])
suit = data[1]
res = 0
for i in range(4*n):
    line = input()
    if line[1] == suit:
        res += dominant[line[0]]
    else:
        res += non_dominant[line[0]]
print(res)