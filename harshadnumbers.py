def is_harshad(n):
    digit_sum = 0
    n_copy = n
    while n != 0:
        digit_sum += n % 10
        n //= 10
    if n_copy % digit_sum == 0:
        return True
    return False
n = int(input())
while True:
    if is_harshad(n):
        print(n)
        break
    n += 1