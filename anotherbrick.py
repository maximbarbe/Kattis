h, w, n = map(int, input().split(" "))
cur_sum = 0
walls = 0
vals = [*map(int, input().split(" "))]
for i in range(len(vals)):

    if cur_sum + vals[i] > w:
        print("NO")
        exit()
        
    else:
        cur_sum += vals[i]
    
    
    if cur_sum == w:
        walls += 1
        cur_sum = 0
    if walls == h:
        print("YES")
        exit()
if cur_sum != 0 or walls != h:
    print("NO")
else:
    print("YES")