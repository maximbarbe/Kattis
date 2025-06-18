t, h = 0, 0
for char in input():
    if char == "T":
        t += 1
    else:
        h += 1
    if t >= 11 and t - h >= 2 or h >= 11 and h - t >= 2:
        t, h =0, 0
print(f"{t}-{h}")