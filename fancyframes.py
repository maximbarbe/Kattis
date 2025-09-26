a, b, c, d = input().split()
c = int(c)
d = int(d)

for i in range(c):
    print(b*((len(a) + 2 * d) + 2*c))
for i in range(d):
    print(b*c + " "*(len(a) + 2*d) + b*c)
print(b * c + " "*d + a + " "*d + b*c)
for i in range(d):
    print(b*c + " "*(len(a) + 2*d) + b*c)
for i in range(c):
    print(b*((len(a) + 2 * d) + 2*c))