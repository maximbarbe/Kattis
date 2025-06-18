n1 = int(input())
n2 = int(input())


left_rotation = (n1 - n2)%360
right_rotation = (n2 - n1)%360
if left_rotation < right_rotation:
    print(-left_rotation)
else:
    print(right_rotation)