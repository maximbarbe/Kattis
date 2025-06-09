vals = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
num = input()
cur_digit = 0
res = 0
for i in range(len(num)):
    if num[i] != "-":
        res += int(num[i]) * vals[cur_digit]
        cur_digit += 1
if res % 11 == 0:
    print(1)
else:
    print(0)