from math import ceil, floor

n = int(input())
if n % 2 == 0:
    upper_bound = n // 2
else:
    upper_bound = ceil(n/2)
    
def is_valid(n, big, small):
    num_big = 0
    num_small = 0
    while True:
        if n < small:
            break
        if n >= big:
            n -= big
            num_big += 1
        if n < small:
            break
        else:
            n -= small
            num_small += 1
    if n != 0 or num_big - num_small not in [0, 1]:
        return False
    else:
        return True
            
print(f"{n}:")
for i in range(2, upper_bound + 1):

    if is_valid(n, i, i-1):
        print(f"{i},{i - 1}")
    if is_valid(n, i, i):
        print(f"{i},{i}")