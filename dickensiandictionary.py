left = "qwertasdfgzxcvb"
right = "yuiophjklnm"

s = input()

prev = None

for c in s:
    if c in left:
        if prev == "left":
            print("no")
            exit()
        prev = "left"
    else:
        if prev == "right":
            print("no")
            exit()
        prev = "right"
print("yes")