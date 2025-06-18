c, n = map(int, input().split(" "))
cur = 0
impossible = False
for i in range(n):
    left, entered, stay = map(int, input().split(" "))
    cur -= left
    if cur < 0:
        impossible = True
    cur += entered
    if cur > c:
        impossible = True
    if stay != 0 and cur != c:
        impossible = True

if cur > 0:
    impossible = True
if impossible:
    print("impossible")
else:
    print("possible")