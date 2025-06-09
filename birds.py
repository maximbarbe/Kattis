import math
def read_problem():
    lines = input().strip("\n").split(" ")
    length = int(lines[0])
    distance_between_pillars = int(lines[1])
    num_pillars = int(lines[2])
    pillars = []
    if num_pillars != 0:
        for i in range(num_pillars):
            pillars.append(int(input()))
    pillars.sort()
    return length, distance_between_pillars, num_pillars, pillars


def num_pillars_to_add(length, distance_between_pillars, distance_from_extremities, pillars):
    cur = distance_from_extremities
    pillars_to_add = 0
    while True:
        if cur + distance_from_extremities > length:
            return pillars_to_add
        else:
            if pillars and abs(cur - pillars[0]) < distance_between_pillars:
                cur = pillars[0] + distance_between_pillars
                pillars.pop(0)
            else:
                if pillars:
                    pillars_to_add += math.floor((pillars[0] - cur)/distance_between_pillars)
                    cur += distance_between_pillars * math.floor((pillars[0] - cur)/distance_between_pillars)
                else:
                    pillars_to_add += math.floor((length - distance_from_extremities - cur)/distance_between_pillars) + 1
                    return pillars_to_add       


def main():

    length, distance_between_pillars, num_pillars, pillars = read_problem()


    n = num_pillars_to_add(length, distance_between_pillars, 6, pillars)
    print(n)
    # Vous pouvez découper votre code en d'autres fonctions...
    # You may split your code in other functions...

main()