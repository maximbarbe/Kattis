n = int(input())
dist = float(input())
efficiencies = []
winner_name = None
winner_eff = -1
for i in range(n):
    initial, vel, fuel = input().split()
    fuel = float(fuel)
    vel = float(vel)
    rof = fuel / (dist/vel)
    eff = vel / rof
    if eff > winner_eff:
        winner_eff = eff
        winner_name = initial
print(winner_name)