n = int(input())
for i in range(n):
    numbers = list(map(int, [char for char in input()]))
    for i in range(len(numbers) -2, -1, -2):
        cur = numbers[i] * 2
        if cur >= 10:
            cur = int(str(cur)[0]) + int(str(cur)[1])
        numbers[i] = cur
        
    sumn = sum(numbers)
    if sumn % 10 == 0:
        print("PASS")
    else:
        print("FAIL")