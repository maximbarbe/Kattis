n = int(input())
vertical = {i:False for i in range(n)}
horizontal = {i:False for i in range(n)}
left_diagonal = {i:False for i in range(2*n)}
right_diagonal = {i:False for i in range(2*n)}
for i in range(n):
    x, y = map(int, input().split(" "))
    left = (n-1)-x + y + 1
    right = x + y + 1
    if vertical[y] or horizontal[x] or left_diagonal[left] or right_diagonal[right]:
        print("INCORRECT")
        exit()
    vertical[y] = True
    horizontal[x] = True
    left_diagonal[left] = True
    right_diagonal[right] = True
else:
    print("CORRECT")