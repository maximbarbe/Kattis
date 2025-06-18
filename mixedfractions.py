while True:
    num, denum = map(int, input().split(" "))
    if num == denum == 0:
        break
    print(f"{num//denum} {num%denum} / {denum}")