n = int(input())
digits = [int(digit) for digit in str(n)]
lower = digits.copy()
upper = digits.copy()
left, right = 0, len(lower) - 1
while left != right:
    while left != len(lower):
        if left == 0:
            if lower[left] == 1:
                left += 1
            else:
                break
        else:
            if lower[left] == 0:
                left += 1
            else:
                break
    while right != -1:
        if lower[right] == 9:
            right -= 1
        else:
            break
    
    
    
    if left == right or left > right:
        break
    else:
        lower[left] -= 1
        lower[right] += 1
        
left= 0
right = len(upper) - 1
while left != right:
    while left != len(upper):
        if upper[left] == 9:
            left += 1
        else:
            break
    while right != -1:
        if upper[right] == 0:
            right -= 1
        else:
            break
    
    
    
    if left == right or left > right:
        break
    else:
        upper[left] += 1
        upper[right] -= 1    

        
print("".join(map(str, lower)), "".join(map(str, upper)))
    