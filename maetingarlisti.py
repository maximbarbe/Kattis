n, r, c=  map(int, input().split())
rows = []
for i in range(r):
    rows.append(input().split())
    
cur_row = []
idx = 0
for i in range(r*c):
    cur_row.append(input())
    if len(cur_row) == c:
        if cur_row == rows[idx]:
            print("left")
        else:
            print("right")
        cur_row = []
        idx += 1
