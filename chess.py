n = int(input())


def get_accessible_pos(row_src, col_src):
    temp_row = row_src
    temp_col = col_src
    accessible_pos = set([(temp_row, temp_col)])
    
    while temp_row - 1 >= 0 and temp_col -1 >= 0:
        accessible_pos.add((temp_row - 1, temp_col - 1))
        temp_row -= 1
        temp_col -= 1

    temp_row = row_src
    temp_col = col_src
    
    while temp_row - 1 >= 0 and temp_col + 1 < 8:
        accessible_pos.add((temp_row - 1, temp_col + 1))
        temp_row -= 1
        temp_col += 1
        
    temp_row = row_src
    temp_col = col_src  
    
    while temp_row + 1 < 8 and temp_col - 1 >= 0:
        accessible_pos.add((temp_row + 1, temp_col - 1))
        temp_row += 1
        temp_col -= 1
        
    temp_row = row_src
    temp_col = col_src  
        
    while temp_row + 1 < 8 and temp_col +1 < 8:
        accessible_pos.add((temp_row + 1, temp_col + 1))
        temp_row += 1
        temp_col += 1      
    return accessible_pos
        
        

for i in range(n):
    col_letter1, row1, col_letter2, row2 = input().split()
    row_src = int(row1) - 1
    col_src = ord(col_letter1) - ord('A')
    
    row_dest = int(row2) - 1
    col_dest = ord(col_letter2) - ord('A')
    
    if row_src % 2 == row_dest % 2:
        if col_src % 2 != col_dest % 2:
            print("Impossible")
            continue
    else:
        if col_src % 2 == col_dest % 2:
            print("Impossible")
            continue
    if row_src == row_dest and col_src == col_dest:
        print(0, chr(col_src + ord('A')), row_src + 1)
        continue

    
    accessible_pos_from_1 = get_accessible_pos(row_src, col_src)
    accessible_pos_from_2 = get_accessible_pos(row_dest, col_dest)
    
    if (row_dest, col_dest) in accessible_pos_from_1:
        print(1, chr(col_src + ord('A')), row_src + 1, chr(col_dest + ord('A')), row_dest + 1)
    else:
        intersect = list(accessible_pos_from_1.intersection(accessible_pos_from_2))[0]
        print(2, chr(col_src + ord('A')), row_src + 1, chr(intersect[1] + ord('A')), intersect[0] + 1, chr(col_dest + ord('A')), row_dest + 1)