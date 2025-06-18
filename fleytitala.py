n = int(input())
bounces = int(input())
length = n
if n == 0:
    print("0.0")
elif bounces == 0:
    print(length)
else:
    print(length + length*(1-pow(1/2, bounces)))
