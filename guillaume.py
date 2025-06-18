n = int(input())
cur_wins = 0
cur_losses = 0

max_percent_wins = 0
max_percent_losses = 0
max_win_percentage = -1
matches = 0
string = input()
for i in range(len(string) - 1, -1, -1):
    if string[i] == 'G':
        cur_wins += 1
        matches += 1
    elif string[i] == "A":
        cur_losses += 1
        matches += 1
    if matches == 0:
        continue
    if (cur_wins)/matches > max_win_percentage:
        max_win_percentage = (cur_wins)/matches
        max_percent_wins = cur_wins
        max_percent_losses = cur_losses
print(f"{max_percent_wins}-{max_percent_losses}")