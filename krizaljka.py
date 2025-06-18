first, second = input().split(" ")
for i in range(len(first)):
    if first[i] in second:
        first_idx = i
        second_idx = second.index(first[i])
        break
        
for i in range(len(second)):
    for j in range(len(first)):
        if j != first_idx and i != second_idx:
            print(".", end="")
        elif j == first_idx  and i != second_idx:
            print(second[i],end="")
        else:
            print(first[j], end="")
    print()