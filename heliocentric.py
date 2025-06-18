import sys
case = 0
for line in sys.stdin:
    case += 1
    earth, mars = map(int, line.strip("\n").split(" "))
    days = 0
    while earth != 0 or mars != 0:
        earth = (earth + 1)%365
        mars = (mars + 1)%687
        days += 1
    print(f"Case {case}: {days}")