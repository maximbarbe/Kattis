ordering = input().split(" ")

while True:
    
    if ordering[0] > ordering[1]:
        ordering[0], ordering[1] = ordering[1], ordering[0]
        print(" ".join(ordering))
    if ordering[1] > ordering[2]:
        ordering[1], ordering[2] = ordering[2], ordering[1]
        print(" ".join(ordering))
    if ordering[2] > ordering[3]:
        ordering[2], ordering[3] = ordering[3], ordering[2]
        print(" ".join(ordering))
    if ordering[3] > ordering[4]:
        ordering[3], ordering[4] = ordering[4], ordering[3]
        print(" ".join(ordering))
    if ordering == ["1", "2", "3", "4", "5"]:
        break