from itertools import permutations
from datetime import datetime


def is_leap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

t = int(input())
for i in range(t):
    digits = []
    date = input().split()
    for _ in date:
        for char in _:
            digits.append(char)
    dates = set()
    for p in permutations(digits):
        day = int(p[0] + p[1])
        month = int(p[2] + p[3])
        year = int(p[4] + p[5] + p[6] + p[7])
        if year < 2000:
            continue
        try:
            datetime(year=year, month=month, day=day)
            dates.add((year, month, day))
        except:
            continue
    
    if len(dates) == 0:
        print(0)
    else:
        minimum = min(dates)
        print(len(dates), str(minimum[2]).zfill(2), str(minimum[1]).zfill(2), str(minimum[0]).zfill(2))