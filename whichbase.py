def base_to_dec(digit_string, base):
    res = 0
    for i in range(len(digit_string)):
        if int(digit_string[i]) >= base:
            return 0
        else:
            res += int(digit_string[i]) * pow(base, len(digit_string) - 1 - i)
    return res

n = int(input())
for i in range(n):
    k, val = input().split(" ")
    print(f"{k} {base_to_dec(val, 8)} {int(val)} {base_to_dec(val, 16)}")