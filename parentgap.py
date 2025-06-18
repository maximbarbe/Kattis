import calendar

year = int(input())
print(f"{(max(calendar.monthcalendar(year, 5)[-1]) - calendar.monthcalendar(year, 5)[1][-1] + calendar.monthcalendar(year, 6)[2][-1])//7} weeks")