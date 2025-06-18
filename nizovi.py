string = input()
tabs = 0
for i, char in enumerate(string):
    if char == "}":
        tabs -= 2
        print()
        print(" "*tabs+char, end="")
    else:
        if char == "{":
            
            if string[i + 1] != "}":
                tabs += 2
                print(char)
                print(" "*tabs, end="")
            else:
                tabs += 2
                print(char, end="")
        elif char == ",":
            print(char)
            print(" "*tabs, end="")
        else:
            print(char, end="")
print()