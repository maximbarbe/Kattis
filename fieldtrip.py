from collections import Counter


n = int(input())
vals = [*map(int, input().split(" "))]

# If the bus are identical, then each bus gets 1 third of the people.

people_per_bus = sum(vals)/3
first_bus = None
second_bus = None
third_bus = None
cur = 0
for i in range(len(vals)):
    if cur + vals[i] > people_per_bus:
        print(-1)
        exit()
    elif cur+vals[i] == people_per_bus:
        if first_bus == None:
            first_bus = i + 1
        elif second_bus == None:
            second_bus = i + 1
        elif third_bus == None:
            third_bus = i + 1
        else:
            print(-1)
            exit()
        cur = 0
    else:
        cur += vals[i]
else:
    if cur != 0 or first_bus == None or second_bus == None:
        print(-1)
    else:
        print(f"{first_bus} {second_bus}")