calls = 0
while True:
    n = int(input())
    if n == 0:
        break
    if calls != 0:
        print()
    calls += 1

    am_times = []
    am12_times = []
    pm_times = []
    pm12_times = []
    for i in range(n):
        time, am_pm = input().split(" ")
        hour, minutes = time.split(":")
        hour = int(hour)
        if hour == 12:
            if am_pm == "a.m.":
                am12_times.append((hour, minutes, am_pm))
            else:
                pm12_times.append((hour, minutes, am_pm))
        else:
            if am_pm == "a.m.":
                am_times.append((hour, minutes, am_pm))
            else:
                pm_times.append((hour, minutes, am_pm))
    am12_times.sort(key=lambda el: el[1])
    pm12_times.sort(key=lambda el:el[1])
    am_times.sort(key=lambda el:(el[0], el[1]))
    pm_times.sort(key = lambda el:(el[0], el[1]))
    times = am12_times +  am_times + pm12_times + pm_times
    for el in times:
        print(f"{':'.join([str(el[0]), el[1]])} {el[2]}")