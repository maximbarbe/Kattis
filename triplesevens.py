import sys
n = int(input())
for line in sys.stdin:
    wheel = line.strip("\n").split(" ")
    found = False
    for char in wheel:
        if char == "7":
            found = True
    if not found:
        print("0")
        exit()
else:
    print("777")