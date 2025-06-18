day = 1
start = 1
end = int(input())
while True:
    mid = (start + end)//2
    print(mid * day)
    res = input()
    if res == "less":
        end = mid
    elif res == "more":
        start = mid + 1
    else:
        exit()
    day += 1