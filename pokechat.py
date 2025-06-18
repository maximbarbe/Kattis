encoding = input()
digits = input()

for i in range(len(digits)//3):
    print(encoding[int(digits[3*i:3*i+3]) - 1], end="")
print()