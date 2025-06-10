c, x, m = map(float, input().split())
indices = {
    0:55,
    1: 60,
    2:65,
    3:70,
    4:75,
    5:80
}
c/=2
efficiencies = []
for i in range(6):
    _, eff = map(float, input().split())
    efficiencies.append(eff)
    
for i in range(5, -1, -1):
    eff = efficiencies[i]
    gallons_needed = m/eff
    if gallons_needed > c:
        continue
    time_needed = m / indices[i]
    lost_fuel = x * time_needed
    if gallons_needed + lost_fuel <= c:
        print("YES", indices[i])
        exit()
else:
    print("NO")