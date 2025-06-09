months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_idx = 3
day, month = map(int, input().split(" "))
d = day + sum(months[:month - 1]) - 1
print(days[(day_idx + d) % 7])