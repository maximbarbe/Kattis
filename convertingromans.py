n = int(input())
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

for i in range(n):
    res = 0
    m = 0
    cur = input()
    for char in cur[::-1]:
        if values[char] < m:
            res -= values[char]
        else:
            res += values[char]
            m = max(m, values[char])
    print(res)