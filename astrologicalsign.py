n = int(input())
for i in range(n):
    date, month = input().split(" ")
    date = int(date)
    if month == "Jan":
        if date <= 20:
            print("Capricorn")
        else:
            print("Aquarius")
    elif month == "Feb":
        if date <= 19:
            print("Aquarius")
        else:
            print("Pisces")
    elif month == "Mar":
        if date <= 20:
            print("Pisces")
        else:
            print("Aries")
    elif month == "Apr":
        if date <= 20:
            print("Aries")
        else:
            print("Taurus")
    elif month == "May":
        if date <= 20:
            print("Taurus")
        else:
            print("Gemini")
    elif month == "Jun":
        if date <= 21:
            print("Gemini")
        else:
            print("Cancer")
    elif month == "Jul":
        if date <= 22:
            print("Cancer")
        else:
            print("Leo")
    elif month == "Aug":
        if date <= 22:
            print("Leo")
        else:
            print("Virgo")
    elif month == "Sep":
        if date <= 21:
            print("Virgo")
        else:
            print("Libra")
    elif month == "Oct":
        if date <= 22:
            print("Libra")
        else:
            print("Scorpio")
    elif month == "Nov":
        if date <= 22:
            print("Scorpio")
        else:
            print("Sagittarius")
    elif month == "Dec":
        if date <= 21:
            print("Sagittarius")
        else:
            print("Capricorn")