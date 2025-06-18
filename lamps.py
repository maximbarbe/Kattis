from math import ceil
h, p = map(int, input().split())
for i in range(1, 8001):
    inc_needed = ceil((i*h)/1000)
    k_i = (60*h*i*p)/100000
    k_l = (11*h*i*p)/100000
    if (inc_needed * 5) + k_i > 60 + k_l:
        print(i)
        exit()
else:
    print(8000)