first = True
while True:
    data = input().split(" ")
    if data[0] == "0":
        break
    if not first:
        print()
    first = False
    n, m = map(int, data)

    scores = {i:[0, 0] for i in range(1, n+1)}
    for i in range((m*n*(n-1))//2):
        p1, choice1, p2, choice2 = input().split(" ")
        if choice1 == "rock":
            if choice2 == "paper":
                scores[int(p2)][0] += 1
                scores[int(p1)][1] += 1
            elif choice2 == "scissors":
                scores[int(p2)][1] += 1
                scores[int(p1)][0] += 1
        elif choice1 == "paper":
            if choice2 == "scissors":
                scores[int(p2)][0] += 1
                scores[int(p1)][1] += 1
            elif choice2 == "rock":
                scores[int(p2)][1] += 1
                scores[int(p1)][0] += 1
        else:
            if choice2 == "rock":
                scores[int(p2)][0] += 1
                scores[int(p1)][1] += 1
            elif choice2 == "paper":
                scores[int(p2)][1] += 1
                scores[int(p1)][0] += 1
    for key, val in scores.items():
        if sum(val) == 0:
            print("-")
        else:
            print(f"{val[0]/sum(val):.3f}")