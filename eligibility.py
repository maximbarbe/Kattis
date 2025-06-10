n = int(input())
for i in range(n):
    name, began, birth, courses = input().split(" ")
    courses = int(courses)
    if int(began[:4])>= 2010 or int(birth[:4]) >= 1991:
        print(f"{name} eligible")
    else:
        if courses >= 41:
            print(f"{name} ineligible")
        else:
            print(f"{name} coach petitions")