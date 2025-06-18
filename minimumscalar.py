n = int(input())
case_num = 1
for i in range(n):
    m = int(input())
    res = 0
    first = [*map(int, input().split(" "))]
    second = [*map(int, input().split(" "))]
    first.sort()
    second.sort(reverse=True)
    for i in range(m):
        res += first[i] * second[i]
    print(f"Case #{case_num}: {res}")
    case_num += 1