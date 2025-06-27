ones = 0
twos = 0
res = 0
s = input()
for c in s:
    if c == "2":
        twos += 1
    elif c == "1":
        res += twos
        ones += 1
    else:
        res += twos + ones
        
print(res)