PI = 3.14159
d = float(input())
w = float(input())
n = int(input())
if n*w <= 2*PI*(d/2):
    print("YES")
else:
    print('NO')