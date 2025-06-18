first = input()
second = input()
x = first.count("S")
y = second.count("S")
if x == 0 or y == 0:
    print(0)
    exit()
print(f"{'S(' * (x*y)}0{')' * (x*y)}")