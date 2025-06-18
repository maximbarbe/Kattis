n = int(input())
if n == 1:
    print("Either")
elif n == 2:
    print("Odd")
elif n == 10 or n == 6:
    print('Odd')
else:
    if n % 2==0:
        print("Even")
    else:
        print('Either')