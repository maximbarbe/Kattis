from math import sqrt, floor
while True:
    try:
        n = int(input())
    except EOFError:
        break
    
    factors = [1]

    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            if i**2 == n:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(n//i)
    sum_n = sum(factors)
    if sum_n == n:
        print(f"{n} perfect")
    elif abs(n - sum_n) <= 2:
        print(f"{n} almost perfect")
    else:
        print(f"{n} not perfect")