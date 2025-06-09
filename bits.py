n = int(input())
for i in range(n):
    max_count = 0
    num = input()
    cur_num = ""
    for char in num:
        cur_num += char
        num_ones = bin(int(cur_num)).count("1")
        if num_ones > max_count:
            max_count = num_ones
        
    print(max_count)