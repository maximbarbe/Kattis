n = int(input())
vals = [*map(int, input().split())]
vals.sort()
first = vals[:len(vals)//3]
sec = vals[len(vals)//3:(2*len(vals))//3]
third = vals[(2*len(vals))//3:]
print(*sec, *first, *third)