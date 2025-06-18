from collections import Counter


def compare_digits(x, y):

    x_conv = str(x)
    y_conv = str(y)
    combined_digits = Counter(x_conv + y_conv)
    mult = Counter(str(x*y))
    return combined_digits == mult
A, B = map(int, input().split(" "))
res = 0
pairs = []
for i in range(A, B + 1):
    for j in range(i, B+1):
        if compare_digits(i, j):
            res += 1
            pairs.append((i, j))
print(f"{res} digit-preserving pair(s)")
for i in range(len(pairs)):
    print(f"x = {pairs[i][0]}, y = {pairs[i][1]}, xy = {pairs[i][0] * pairs[i][1]}")