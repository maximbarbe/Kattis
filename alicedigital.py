from math import inf
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    vals = [*map(int, input().split())]
    max_weight = -inf
    start = 0
    end= 0
    cur_sum = 0
    found = False
    while end != len(vals):
        if vals[end] > m:
            cur_sum += vals[end]
            end += 1
        elif vals[end] < m:
            cur_sum = 0
            found = False
            end += 1
            start = end
        else:
            if found == False:
                found = True
                cur_sum += m
                end += 1
            else:
                while vals[start] != m:
                    cur_sum -= vals[start]
                    start += 1
                start += 1
                end += 1
        if cur_sum > max_weight and found:
            max_weight = cur_sum
    print(max_weight)