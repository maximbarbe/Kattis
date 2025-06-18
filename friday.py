t = int(input())
for i in range(t):
    days, m = input().split()
    months = [*map(int, input().split())]
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    start_idx = -1
    res = 0
    for val in months:
        if val < 13:
            start_idx = (start_idx + val)%7
        else:
            start_idx = (start_idx + 13)%7
            if week[start_idx] == "Friday":
                res += 1
            start_idx = (start_idx + (val - 13))%7
    print(res)