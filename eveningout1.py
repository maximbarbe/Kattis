A, B = map(int, input().split(" "))
print(min(A % B, B - (A % B)))