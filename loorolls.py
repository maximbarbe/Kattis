l, n = map(int, input().split(" "))
k = 1
cur_roll = l
while True:
    if cur_roll % n == 0:
        print(k)
        exit()
    else:
        k += 1
        n -= cur_roll % n