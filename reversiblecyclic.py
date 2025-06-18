string = input()
reverse = (string + string)[::-1]
if string[:-1] in reverse:
    print(1)
else:
    print(0)