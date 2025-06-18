n, a, b = map(int, input().split(" "))
values = []
for i in range(n-1):
    values.append(int(input()))
    
if a in values and b in values:
    for i in range(a, b + 1):
        print(i)
elif a in values and b not in values:
    print(b)
elif a not in values and b in values:
    print(a)
else:
    print(-1)