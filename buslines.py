from collections import defaultdict
n, m = map(int, input().split(" "))
if m < n - 1:
    print(-1)
    exit()
else:
    sums = defaultdict(lambda:False)
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if sums[i +j] == False:
                sums[i + j] = True
                
    if m > len(sums.keys()):
        print(-1)
        exit()
    cur_edges = 0
    taken_sums = defaultdict(lambda:False)
    for i in range(1, n):
        for j in range(i+1, n+1):
            if cur_edges == m:
                exit()
            else:
                if taken_sums[i + j] == False:
                    print(f"{i} {j}")
                    taken_sums[i + j] = True
                    cur_edges += 1