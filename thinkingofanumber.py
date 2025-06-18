from math import inf
while True:
    lower_bound = 1
    upper_bound = inf
    divisors = set()
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        data = input().split()
        if data[0] == "less":
            upper_bound = min(int(data[2]), upper_bound)
        elif data[0] == "greater":
            lower_bound = max(lower_bound, int(data[2]) + 1)
        else:
            divisors.add(int(data[2]))
    nums = []
    if upper_bound == inf:
        print("infinite")
    else:
        for i in range(lower_bound, upper_bound):
            for div in divisors:
                if i % div != 0:
                    break
            else:
                nums.append(i)
        if nums == []:
            print("none")
        else:
            print(" ".join(map(str, nums)))