N, P, X, Y = map(int, input().split(" "))
res = 0
current_read = 0
page_num = 0
while current_read <= P:
    if (page_num + 1) % N == 0:
        page_num += 1
        res += Y
    else:
        page_num += 1
        current_read += 1
        res += X

print(res- X)