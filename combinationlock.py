while True:
    res = 0
    init, first, sec, third = map(int, input().split(" "))
    if init == first == sec == third == 0:
        break
    res += 720
    if first > init:
        res += 9 * (init + 40 - first)
    else:
        res += (9 * (init - first))
    if sec < first:
        res += 9 * (sec + 40 - first)
    else:
        res += 9 * (sec - first)
    if third > sec:
        res += 9 * (sec + 40 - third)
    else:
        res += (9 * (sec - third))
        
    res += 360

    print(res)