n, k, q = map(int, input().split(" "))
for i in range(q):
    start, finish = map(int, input().split(" "))
    start -=1
    finish -= 1
    res = 0
    while start != finish:
        if start < finish:
            finish = (finish - 1)//k
            res += 1
        else:
            start = (start - 1)//k
            res += 1
    print(res)