low, high = 1, 1000
guesses_left = 10
while guesses_left != 0:
    mid = (low + high)//2
    print(mid)
    guesses_left -= 1
    answer = input()
    if answer == "lower":
        high = mid
    elif answer == "higher":
        low = mid + 1
    else:
        exit()