L, H = map(int, input().split(" "))
res = 0
for c in range(L, H+1):
    str_rep = str(c)
    if len(set(str_rep)) != len(str_rep)  or "0"  in str_rep:
        continue
    digits = [int(char) for char in str(c)]
    for digit in digits:
        if c % digit != 0:
            break
    else:
        res += 1
print(res)