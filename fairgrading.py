x, y, z = map(int, input().split())
avg = 0.25*x + 0.25*y +0.5*z
if 90 <= avg <= 100:
    print("A")
elif 80 <= avg < 90:
    print('B')
elif 70 <= avg < 80:
    print("C")
elif 60 <= avg < 70:
    print("D")
else:
    print('F')