while True:
    s0, s1, r0, r1 = input().split()
    if s0 == "0" and s1 == "0" and r0 == "0" and r1 == "0":
        break
    first = "".join(sorted(s0 + s1, reverse=True))
    second = "".join(sorted(r0 + r1, reverse=True))
    
    if first == "21" or second == "21":
        if first == "21" and second == "21":
            print("Tie.")
        else:
            print(f"Player {'1' if first == '21' else '2'} wins.")
    elif first[0] == first[1] or second[0] == second[1]:
        if first[0] == first[1] and second[0] == second[1]:
            if first == second:
                print("Tie.")
            else:
                print(f"Player {'1' if first > second else '2'} wins.")
        else:
            print(f"Player {'1' if first[0] == first[1] else '2'} wins.")
    else:
        if first == second:
            print("Tie.")
        else:
            print(f"Player {'1' if first > second else '2'} wins.")