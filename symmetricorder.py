set_num = 1
while True:
    n = int(input())
    if n == 0:
        break
    names = []
    for i in range(n):
        names.append(input())
    print(f"SET {set_num}")
    start = 0
    while start < len(names):
        print(names[start])
        start += 2
    if (len(names) - 1) % 2 == 0:
        end = len(names) - 2
    else:
        end = len(names) - 1
    while end > 0:
        print(names[end])
        end -= 2
    set_num += 1