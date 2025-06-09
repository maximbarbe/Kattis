import datetime
import itertools

data1 = input()
data = [*map(int, data1.split("/"))]
perms = list(itertools.permutations(data, 3))
perms.sort(key=lambda el:(el[0], el[1], el[2]))

for el in perms:
    try:

        datetime.datetime(year=el[0] + 2000 if el[0] < 1000 else el[0],month = el[1], day=el[2])
        date = [str(el[0] + 2000 if el[0] < 1000 else el[0]), str(el[1]), str(el[2])]
        print(f"{date[0]}-{'0' if len(date[1]) == 1 else ''}{date[1]}-{'0' if len(date[2]) == 1 else ''}{date[2]}")
        exit()
    except ValueError:
        continue
else:
    print(f"{data1} is illegal")