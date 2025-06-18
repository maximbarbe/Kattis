t = int(input())
for i in range(t):
    l1 = [*map(int, input().split())]
    l2 = [*map(int, input().split())]
    found = False
    for j in range(5):
        for k in range(5):
            if l1[j] == l2[k] and j != k:
                print("YES")
                break
        else:
            continue
        break
    else:
        print('NO')