def out_shuffle(n):
    deck = [i for i in range(n)]
    shuffled = deck.copy()
    half = n//2
    if n % 2 == 1:
        first_half = shuffled[:half + 1]
        second_half = shuffled[half + 1:]
        shuffled = []
        for i in range(len(second_half)):
            shuffled.append(first_half[i])
            shuffled.append(second_half[i])
        else:
            shuffled.append(first_half[-1])
    else:
        first_half = shuffled[:half]
        second_half = shuffled[half:]
        shuffled = []
        for i in range(len(second_half)):
            shuffled.append(first_half[i])
            shuffled.append(second_half[i])

            
    res = 1
    while shuffled != deck:
        if n % 2 == 1:
            first_half = shuffled[:half + 1]
            second_half = shuffled[half + 1:]
            shuffled = []
            for i in range(len(second_half)):
                shuffled.append(first_half[i])
                shuffled.append(second_half[i])
            else:
                shuffled.append(first_half[-1])
        else:
            first_half = shuffled[:half]
            second_half = shuffled[half:]
            shuffled = []
            for i in range(len(second_half)):
                shuffled.append(first_half[i])
                shuffled.append(second_half[i])
        res += 1
    return res

def in_shuffle(n):
    deck = [i for i in range(n)]
    shuffled = deck.copy()
    half = n // 2
    first_half = shuffled[:half]
    second_half = shuffled[half:]
    shuffled = []
    for i in range(len(first_half)):
        shuffled.append(second_half[i])
        shuffled.append(first_half[i])
        
    else:
        if n % 2 == 1:
            shuffled.append(second_half[-1])
    res = 1
    while shuffled != deck:
        first_half = shuffled[:half]
        second_half = shuffled[half:]
        shuffled = []
        for i in range(len(first_half)):
            shuffled.append(second_half[i])
            shuffled.append(first_half[i])
            
        else:
            if n % 2 == 1:
                shuffled.append(second_half[-1])
        res += 1
    return res

n, type = input().split()

n = int(n)
match type:
    case "out":
        print(out_shuffle(n))
        
    case _:
        print(in_shuffle(n))
