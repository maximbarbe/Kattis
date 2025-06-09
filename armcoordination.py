x,y = map(int, input().split(" "))
r = int(input())
x_1 = x - r
y_1 = y + r
x_2 = x + r
y_2 = y_1
x_3 = x_2
y_3 = y - r
x_4 = x_1
y_4 = y_3
print(f"{x_1} {y_1}")
print(f"{x_2} {y_2}")
print(f"{x_3} {y_3}")
print(f"{x_4} {y_4}")