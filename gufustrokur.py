a = int(input())
b = int(input())
print(min(abs(b - a), abs(b - (a + 360)), abs(a - (360+b))))