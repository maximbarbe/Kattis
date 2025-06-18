import sys
for line in sys.stdin:
    line = line.strip("\n").split(" ")
    for word in line:
        if "problem" in word.lower():
            print("yes")
            break
    else:
        print("no")