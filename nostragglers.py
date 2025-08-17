c = {
    "STU": 0,
    "VIS": 0,
    "FAC": 0
}
for i in range(int(input())):
    type, d, p = input().split()
    if d == "IN":
        c[type] += int(p)
    else:
        c[type] -= int(p)
r = sum(c.values())
if r == 0:
    print("NO STRAGGLERS")
else:
    print(r)
