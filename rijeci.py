n = int(input())
if n == 1:
    print("0 1")
else:
    a = 0
    b = 1
    for i in range(n - 1):
        temp_a = a
        temp_b = b
        b = temp_b + temp_a
        a = temp_b
    print(f"{a} {b}")