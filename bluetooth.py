n = int(input())
left = True
right = True
upper_left = 8
upper_right = 8
bottom_left = 8
bottom_right = 8
for i in range(n):
    data = input().split(" ")
    if data[0][0] == "-":
        if data[1] == "m":
            bottom_left -= 1
        else:
            left = False
    elif data[0][1] == "-":
        if data[1] == "m":
            bottom_right -= 1
        else:
            right = False
    elif data[0][0] == "+":
        if data[1] == "m":
            upper_left -= 1
        else:
            left = False
    else:
        if data[1] == "m":
            upper_right -= 1
        else:
            right = False
if bottom_left == 0 or upper_left == 0:
    left = False
if bottom_right == 0 or upper_right == 0:
    right = False

if left:
    print(0)
elif right:
    print(1)
else:
    print(2)