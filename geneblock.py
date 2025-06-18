digits = {
    "7": 1,
    "4": 2,
    "1": 3,
    "8": 4,
    "5": 5,
    "2": 6,
    "9": 7,
    "6": 8,
    "3": 9,
    "0": 10
            }
n = int(input())
for i in range(n):
    num = input()
    if int(num) < 7 * digits[num[-1]]:
        print(-1)
    else:
        print(digits[num[-1]])