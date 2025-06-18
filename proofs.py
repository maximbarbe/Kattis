from collections import defaultdict
n = int(input())
truth = defaultdict(lambda:False)
for i in range(n):
    first, sec = input().split("-> ")
    if first == "":
        truth[sec] = True
    else:
        first = first.rstrip()
        vals = first.split(" ")
        c = True
        for v in vals:
            c = c and truth[v]
        if not c:
            print(i + 1)
            exit()
        else:
            truth[sec] = True
else:
    print("correct")