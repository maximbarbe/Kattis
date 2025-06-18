while True:
    data = [*map(int, input().split(" "))]
    if data[0] == 0:
        break
    courses = set(map(int, input().split(" ")))
    m = data[1]
    meets_requirements = True
    for i in range(m):
        data = [*map(int, input().split(" "))]
        if len(courses.intersection(set(data[2:]))) < data[1]:
            meets_requirements = False
    if not meets_requirements:
        print("No")
    else:
        print("Yes")