def get_position(left_num, right_num):
    if left_num == right_num:
        return 1
    elif left_num > right_num:
        return 2 * get_position(left_num - right_num, right_num) + 1
    else:
        return 2 * get_position(left_num, right_num - left_num)
        
n = int(input())
for i in range(n):
    m, data = input().split(" ")
    p, q = data.split("/")
    pos = get_position(int(p), int(q))
    print(f"{m} {pos}")