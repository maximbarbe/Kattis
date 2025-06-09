while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    temp_a = a
    temp_b = b
    steps = 0
    seen_a = {}
    while True:
        if a in seen_a:
            break
        else:
            seen_a[a] = steps
            steps += 1
            if a == 1:
                break
            if a % 2 == 0:
                a //= 2
            else:
                a = 3*a + 1
                
    steps = 0
    while True:
        if b in seen_a:
            print(f"{temp_a} needs {seen_a[b]} steps, {temp_b} needs {steps} steps, they meet at {b}")
            break
        else:
            steps += 1
            if b % 2 == 0:
                b //= 2
            else:
                b = 3*b + 1