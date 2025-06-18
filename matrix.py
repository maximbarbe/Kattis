first_line = None
case_num = 1
while True:
    try:
        first_line = input()
    except EOFError:
        exit()
    second_line = input()
    input()
    a, b = map(int, first_line.split(" "))
    c, d = map(int, second_line.split(" "))
    det = a*d - b * c
    print(f"Case {case_num}:")
    print(f"{d//det} {-b//det}")
    print(f"{-c//det} {a//det}")
    case_num += 1