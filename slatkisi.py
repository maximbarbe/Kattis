n, k = map(int, input().split(" "))

smallest_bill = 10 **k

if n % smallest_bill >= smallest_bill/2:
    truncated = n // smallest_bill
    truncated += 1
    n = truncated * smallest_bill
else:
    n = (n // smallest_bill) * smallest_bill
print(n)
