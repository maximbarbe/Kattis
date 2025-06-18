from math import inf

n = int(input())

longest_streak_notnomde = 0
longest_streak_Yraglac = 0

prev = None
cur_streak_notmonde = 0
cur_streak_yraglac= 0

largest_lead_notmonde = 0
largest_lead_yraglac = 0

wins_notmonde = 0
wins_yraglac = 0

for i in range(n):
    name = input()
    if name == "Yraglac":
        wins_yraglac += 1
        if name == prev:
            cur_streak_yraglac += 1
        else:
            cur_streak_yraglac = 1
            cur_streak_notmonde = 0
            prev = name
    else:
        wins_notmonde += 1
        if name == prev:
            cur_streak_notmonde += 1
        else:
            cur_streak_notmonde = 1
            cur_streak_yraglac = 0
            prev = name
    if cur_streak_notmonde > longest_streak_notnomde:
        longest_streak_notnomde = cur_streak_notmonde
    if cur_streak_yraglac  > longest_streak_Yraglac:
        longest_streak_Yraglac = cur_streak_yraglac
    if wins_notmonde - wins_yraglac > largest_lead_notmonde:
        largest_lead_notmonde = wins_notmonde - wins_yraglac
    if wins_yraglac - wins_notmonde > largest_lead_yraglac:
        largest_lead_yraglac = wins_yraglac - wins_notmonde
    
if (longest_streak_notnomde > longest_streak_Yraglac and largest_lead_notmonde > largest_lead_yraglac) or (largest_lead_notmonde == largest_lead_yraglac and longest_streak_notnomde == longest_streak_Yraglac) or (longest_streak_notnomde < longest_streak_Yraglac and largest_lead_notmonde < largest_lead_yraglac):
    print("Agree")
else:
    print("Disagree")