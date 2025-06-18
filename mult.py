n = int(input())
get_first = True
for i in range(n):
    if get_first:
        first = int(input())
        get_first = False
    else:
        val = int(input())
        if val % first == 0:
            print(val)
            get_first = True