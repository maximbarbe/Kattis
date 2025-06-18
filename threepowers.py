while True:
    n = int(input())
    if n == 0:
        break
    nums = []
    cur = 1
    while n != 1:
        if n % 2 == 0:
            nums.append(cur)
        else:
            n += 1
        cur *= 3
        n //=2
    print(f"{{ {', '.join(map(str, nums))} }}")