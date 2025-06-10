def digit_product(num):
    cur = 1
    while num != 0:
        digit = num % 10
        if digit != 0:
            cur *= num % 10
        num //= 10
    if cur >= 10:
        return digit_product(cur)
    return cur
print(digit_product(int(input())))