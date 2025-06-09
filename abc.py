integers = [*map(int, input().split(" "))]
integers.sort()
order = input()
if order == 'ABC':
    print(" ".join(map(str, integers)))
elif order == "ACB":
    print(f"{integers[0]} {integers[2]} {integers[1]}")
elif order == "BAC":
    print(f"{integers[1]} {integers[0]} {integers[2]}")
elif order == "BCA":
    print(f"{integers[1]} {integers[2]} {integers[0]}")
elif order == "CAB":
    print(f"{integers[2]} {integers[0]} {integers[1]}")
elif order == "CBA":
    print(f"{integers[2]} {integers[1]} {integers[0]}")