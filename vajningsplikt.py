arrived, going, other = input().split(" ")
directions = ["North", "West", "South", "East"]
arrived_idx = directions.index(arrived)
going_idx = directions.index(going)
other_idx = directions.index(other)
if going_idx == (arrived_idx + 2)%4 and other_idx == (arrived_idx + 1)% 4:
    print("Yes")
elif going_idx == (arrived_idx - 1) % 4 and other_idx in [(arrived_idx + 2)%4, (arrived_idx + 1)%4]:
    print("Yes")
else:
    print("No")