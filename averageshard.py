n = int(input())
for i in range(n):
    input()
    ncs, ne = map(int, input().split(" "))
    cs = [*map(int, input().split(" "))]
    ne = [*map(int, input().split(" "))]
    cs_sum_scores = sum(cs)
    ne_sum_scores = sum(ne)
    cs_average = cs_sum_scores / len(cs)
    ne_average = ne_sum_scores / len(ne)
    res = 0
    for j in range(len(cs)):
        if (cs_sum_scores - cs[j])/(len(cs) - 1) > cs_average and (ne_sum_scores + cs[j])/(len(ne) + 1) > ne_average:
            res += 1
    print(res)