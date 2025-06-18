symbols = {
    ".": 20,
    "O": 10,
    "\\": 25,
    "/": 25,
    "A": 35,
    "^": 5,
    "v": 22
}
n, m = map(int, input().split(" "))
res = 0
for i in range(n):
    row = input()
    for char in row:
        res += symbols[char]
print(res)