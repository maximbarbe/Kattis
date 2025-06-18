n = int(input())
digits = []

while n not in [1, 2]:
    if n % 2 == 1:
        digits.append("4")
        n -= 1
        n //= 2
    else:
        digits.append("7")
        n -= 1
        n //=2
if n == 1:
    digits.append("4")
else:
    digits.append("7")
print("".join(digits)[::-1])