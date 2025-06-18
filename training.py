n, s = map(int, input().split(" "))
for i in range(n):
    min, max = map(int, input().split(" "))
    if min <= s <= max:
        s += 1
print(s)