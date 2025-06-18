conversion = {"SATT": True, "OSATT": False}
values = {}
n = int(input())
for i in range(n):
    data = input().split()
    match data[0]:
        case "INNTAK":
            values[data[1]] = conversion[data[2]]
        case "UTTAK":
            print(f"{data[1]} {'SATT' if values[data[1]] else 'OSATT'}")
        case "OG":
            values[data[3]] = True if values[data[1]] == True and values[data[2]] == True else False
        case "EDA":
            values[data[3]] = True if values[data[1]] == True or values[data[2]] == True else False
        case "EKKI":
            values[data[2]] = not values[data[1]]