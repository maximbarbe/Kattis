res = 0
for i in range(int(input())):
    s = input()
    if s.startswith("+39") and len(s) - 3 in [9, 10]:
        res += 1
print(res)