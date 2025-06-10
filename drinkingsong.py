n = int(input())
string = input()
for i in range(n, 0, -1):
    if i != 1:
        print(f"{i} bottles of {string} on the wall, {i} bottles of {string}.")
        print(f"Take one down, pass it around, {i-1} bottle{'s' if i - 1 != 1 else ''} of {string} on the wall.")
        print()
    else:
        print(f"{i} bottle of {string} on the wall, {i} bottle of {string}.")
        print(f"Take it down, pass it around, no more bottles of {string}.")