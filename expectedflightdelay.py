day, pwday, pwend, pimp = map(int, input().split())
current_prob = 0
current_day = day - 1
days_before = 0
pwend /= 100
pwday /=100
pimp /= 100
while True:
    current_day = (current_day - 1)%7
    days_before += 1
    if current_day in [0, 6]:
        current_prob = pwend + (1-pwend)*current_prob
    else:
        current_prob = pwday + (1-pwday)*current_prob
    
    if current_prob >= pimp:
        break
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(f"Try to leave on {days[(day - 1 - days_before)%7]}, {days_before} day{('s','')[days_before==1]} before the {days[(day - 1)%7]} meeting.")