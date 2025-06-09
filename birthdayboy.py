from datetime import timedelta
days_before_month = {
    "01": 0,
    "02": 31,
    "03": 59,
    "04": 90,
    "05": 120,
    "06": 151,
    "07": 181,
    "08": 212,
    "09": 243,
    "10": 273,
    "11": 304,
    "12": 334
}

birthday = [False for i in range(365)]
n = int(input())
for i in range(n):
    name, date = input().split()
    month, day = date.split("-")
    birthday[days_before_month[month] + int(day) - 1] = True
max_days_since = 0
temp = []
max_idx = 0
for i in range(365):
    if birthday[i] == True:
        continue
    else:
        days_since = 0
        idx = i
        while birthday[idx] != True:
            idx = (idx - 1)%365
            days_since += 1
        if days_since > max_days_since:
            max_days_since = days_since
            temp = [i]
        elif days_since == max_days_since:
            temp.append(i)
min_diff = 365
max_idx = 0
for idx in temp:
    if idx < 300:
        if idx + 365 - 300 < min_diff:
            min_diff = idx + 365 - 300
            max_idx = idx + 1
    else:
        if idx - 300 < min_diff:
            min_diff = idx - 300
            max_idx = idx + 1
    

if max_idx <= 31:
    print(f"01-{'0' if max_idx < 10 else ''}{max_idx}")
elif max_idx <= 59:
    print(f"02-{'0' if max_idx-31 < 10 else ''}{max_idx-31}")
elif max_idx <= 90:
    print(f"03-{'0' if max_idx-59 < 10 else ''}{max_idx-59}")
elif max_idx <= 120:
    print(f"04-{'0' if max_idx-90 < 10 else ''}{max_idx-90}")
elif max_idx <= 151:
    print(f"05-{'0' if max_idx-120 < 10 else ''}{max_idx-120}")
elif max_idx <= 181:
    print(f"06-{'0' if max_idx-151 < 10 else ''}{max_idx-151}")   
elif max_idx <= 212:
    print(f"07-{'0' if max_idx-181< 10 else ''}{max_idx-181}")
elif max_idx <= 243:
    print(f"08-{'0' if max_idx-212 < 10 else ''}{max_idx-212}")
elif max_idx <= 273:
    print(f"09-{'0' if max_idx-243 < 10 else ''}{max_idx-243}")
elif max_idx <= 304:
    print(f"10-{'0' if max_idx - 273 < 10 else ''}{max_idx - 273}")
elif max_idx <= 334:
    print(f"11-{'0' if max_idx-304 < 10 else ''}{max_idx-304}")
else:
    print(f"12-{'0' if max_idx-334 < 10 else ''}{max_idx-334}")