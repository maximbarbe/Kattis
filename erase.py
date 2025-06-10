n = int(input())
if n % 2 == 1:
    first = input()
    second = input()
    for i in range(len(first)):
        if first[i] == second[i]:
            print("Deletion failed")
            break
    else:
        print("Deletion succeeded")
else:
    first = input()
    second = input()
    for i in range(len(first)):
        if first[i] != second[i]:
            print("Deletion failed")
            break
    else:
        print("Deletion succeeded")