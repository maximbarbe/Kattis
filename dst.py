n = int(input())
for i in range(n):
    dir, num, hours,minutes = input().split(" ")
    num, hours, minutes =int(num), int(hours), int(minutes)
    if dir == "F":
        minutes += num
        if minutes >= 60:
            hours += minutes//60
            minutes %= 60
        hours %= 24
        print(f"{hours} {minutes}")
    else:
        if num > minutes:
            minutes -= num
            
            if minutes < 0:
                hours -= abs(minutes//60) if minutes%60 == 0 else (abs(minutes)//60 + 1)
                minutes %= 60
            hours %= 24
        else:
            minutes -= num
        print(f"{hours} {minutes}")