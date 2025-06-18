k  =0
n = 5
r_a = 0
r_h = 0
a = 0
h = 0
needed = int(input())
for char in input():
    if char == "A":
        a += 1
    else:
        h += 1
    if a == 3:
        a = 0
        h = 0
        r_a += 1
        k = 0
    elif h == 3:
        a = 0
        h = 0
        r_h += 1
        k = 0
        
    if r_a == needed:
        print("Hannes")
        exit()
    elif r_h == needed:
        print("Arnar")
        exit()