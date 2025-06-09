multiples = ["single", "double", "triple"]
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
possible = []
for i in range(len(values)):
    for m in multiples:
        possible.append((m, values[i]))
        
target = int(input())

for i in range(len(possible)):
    cur = 0
    match possible[i][0]:
        case 'single':
            cur += possible[i][1]
        case 'double':
            cur += possible[i][1] * 2
        case _:
            cur += possible[i][1] * 3
    if cur == target:
        print(possible[i][0], possible[i][1])
        exit()
        
for i in range(len(possible)):
    cur = 0
    match possible[i][0]:
        case 'single':
            cur += possible[i][1]
        case 'double':
            cur += possible[i][1] * 2
        case _:
            cur += possible[i][1] * 3
    for j in range(i, len(possible)):
        temp = cur
        match possible[j][0]:
            case 'single':
                temp += possible[j][1]
            case 'double':
                temp += possible[j][1] * 2
            case _:
                temp += possible[j][1] * 3
        if temp == target:
            print(possible[i][0], possible[i][1])
            print(possible[j][0], possible[j][1])
            exit()
            
for i in range(len(possible)):
    cur = 0
    match possible[i][0]:
        case 'single':
            cur += possible[i][1]
        case 'double':
            cur += possible[i][1] * 2
        case _:
            cur += possible[i][1] * 3
    for j in range(i, len(possible)):
        temp1 = cur
        match possible[j][0]:
            case 'single':
                temp1 += possible[j][1]
            case 'double':
                temp1 += possible[j][1] * 2
            case _:
                temp1 += possible[j][1] * 3
        for k in range(j, len(possible)):
            temp2 = temp1
            match possible[k][0]:
                case 'single':
                    temp2 += possible[k][1]
                case 'double':
                    temp2 += possible[k][1] * 2
                case _:
                    temp2 += possible[k][1] * 3
            if temp2 == target:
                print(possible[i][0], possible[i][1])
                print(possible[j][0], possible[j][1])
                print(possible[k][0], possible[k][1])
                exit()
print("impossible")