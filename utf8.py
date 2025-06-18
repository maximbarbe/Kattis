types = [0, 0, 0, 0]
bytes_sequence = []
n = int(input())
for i in range(n):
    bytes_sequence.append(input())
    
i = 0
while i < n:
    if bytes_sequence[i].startswith('0'):
        types[0] += 1
        i += 1
    elif bytes_sequence[i].startswith('110'):
        if i + 1 < n and bytes_sequence[i + 1].startswith('10'):
            types[1] += 1 
            i += 2
        else:
            print('invalid')
            exit()
    elif bytes_sequence[i].startswith('1110'):
        if i + 2 < n and bytes_sequence[i + 1].startswith('10') and bytes_sequence[i + 2].startswith('10'):
            types[2] += 1
            i += 3
        else:
            print('invalid')
            exit()
    elif bytes_sequence[i].startswith('11110'):
        if i + 3 < n and bytes_sequence[i + 1].startswith('10') and bytes_sequence[i + 2].startswith('10') and bytes_sequence[i + 3].startswith('10'):
            types[3] += 1
            i += 4
        else:
            print('invalid')
            exit()
    else:
        print('invalid')
        exit()
        
for i in range(len(types)):
    print(types[i])