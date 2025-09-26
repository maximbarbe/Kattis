l = input()
for char in l:
    if char in "aeiou":
        print(char, end="")
    elif char == "-":
        print()
    elif char in "0123456789":
        print(bin(int(char))[2:], end="")
    else:
        print("beepbloop",end="")
print()