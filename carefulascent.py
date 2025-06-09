xend, yend = map(int, input().split())


def get_final_x(factors, speed, yend):
    curx, cury = 0, 0
    for fact in factors:
        if cury < fact[0]:
            curx += speed * (fact[0] - cury)
            cury = fact[0]
        curx += speed * fact[2] * (fact[1] - fact[0])
        cury = fact[1]
    curx += speed * (yend - cury)
    return curx
factors = []
n = int(input())
for i in range(n):
    start, end, fact = map(float, input().split())
    factors.append((start, end, fact))
start = -10**7
end = 10**7
factors.sort(key = lambda el: el[0])
while True:
    mid = (start + end)/2
    x_val = get_final_x(factors, mid, yend)
    if abs(x_val - xend) < 0.0000005:
        print(mid)
        exit()
    else:
        if x_val < xend:
            start = mid
        else:
            end = mid