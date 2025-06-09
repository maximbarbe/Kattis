p, q = map(int, input().split())
match input():
    case "AABB":
        if q == 7:
            print(8, 9)
            exit()
    case "ABAB":
        if p == 6 and q == 8:
            print(7, 9)
            exit()
    case "ABBA":
        if q - p == 3:
            print(p + 1, q - 1)
            exit()
        
    case "BAAB":
        if p == 2 and q == 8:
            print(1, 9)
            exit()
    case "BABA":
        if p == 2 and q == 4:
            print(1, 3)
            exit()
    case "BBAA":
        if p == 3:
            print(1, 2)
            exit()
        
print(-1)