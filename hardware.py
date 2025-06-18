def get_digits(num, digits):
    global total_digits
    dig = [int(char) for char in str(num)]
    for i in range(len(dig)):
        digits[dig[i]] += 1
        total_digits += 1
    



n = int(input())

for i in range(n):  
    print(input())
    cur = input()
    num_adresses = int(cur.split(" ")[0])
    print(cur)
    cur_adresses = 0
    total_digits = 0
    digits  = {
        0: 0,
        1: 0,
        2: 0,
        3:0,
        4: 0,
        5:0,
        6:0,
        7:0,
        8:0,
        9:0
    }
    while cur_adresses != num_adresses:
        data = input().split(" ")
        if data[0] == "+":
            start = int(data[1])
            end = int(data[2]) + 1
            step = int(data[3])
            for j in range(start, end, step):
                get_digits(j, digits)
                cur_adresses += 1
        else:
            get_digits(int(data[0]), digits)
            cur_adresses += 1
    for key, val in digits.items():
        print(f"Make {val} digit {key}")
    print(f"In total {total_digits} digit{'s' if total_digits > 1 else ''}")