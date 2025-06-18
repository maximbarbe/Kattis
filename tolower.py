p, t = map(int, input().split(" "))
res= 0
for i in range(p):
    problem = False
    for j in range(t):
        s = input()
        converted = s[0].lower() + s[1:]
        if converted != s.lower():
            problem = True
    if problem:
        res += 1
print(p - res)