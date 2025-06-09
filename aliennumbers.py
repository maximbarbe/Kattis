n = int(input())
for i in range(n):
    num, base1, base2 = input().split()
    b1_int = len(base1)
    b2_int = len(base2)
    conv_to_base_10 = 0
    for j in range(len(num) -1, -1, -1):
        conv_to_base_10 += base1.index(num[j]) * b1_int**(len(num) - 1- j)
    res = ""

    while conv_to_base_10 != 0:
        res = base2[conv_to_base_10 % len(base2)] + res
        conv_to_base_10 //= len(base2)
    print(f"Case #{i+1}: {res}")