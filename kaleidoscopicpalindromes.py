def is_palindrome_in_base(num, base):
    dig = []
    while num != 0:
        dig.append(num % base)
        num//= base
    start, end = 0, len(dig) - 1
    while start < end:
        if dig[start] != dig[end]:
            return False
        start += 1
        end -= 1
    return True

a, b, k = map(int, input().split(" "))
res = 0
for i in range(a, b+1):
    for j in range(2, k+1):
        if not is_palindrome_in_base(i, j):
            break
    else:
        res += 1
print(res)