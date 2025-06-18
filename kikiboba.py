string = input()
b = 0
k = 0
for char in string:
    if char == 'b':
        b += 1
    elif char == 'k':
        k += 1
if b == k == 0:
    print("none")
elif b > k:
    print("boba")
elif b < k:
    print("kiki")
else:
    print("boki")