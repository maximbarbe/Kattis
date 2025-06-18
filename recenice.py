conversion = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "onehundred",
    200: "twohundred",
    300: "threehundred",
    400: "fourhundred",
    500: "fivehundred",
    600: "sixhundred",
    700: "sevenhundred",
    800: "eighthundred",
    900: "ninehundred"
}
n = int(input())
if n == 1:
    print("four")
    exit()
words = []
sum_letters = 0
for i in range(n):
    string = input()
    words.append(string)
    sum_letters += len(string)
sum_letters -= 1


for i in range(1, 1000):
    cur = i
    res = ""
    if cur >= 100:
        res += conversion[cur//100 * 100]
        cur -= cur//100 * 100
    if cur >= 20:
        res += conversion[cur//10 * 10]
        cur -= cur//10 * 10
    if cur >= 10:
        res += conversion[cur]
        cur = 0
    if cur >= 1:
        res += conversion[cur]
    if sum_letters + len(res) == i:
        print(" ".join([word if word != "$" else res for word in words]))
        exit()
print(" ".join(words))