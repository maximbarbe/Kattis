string = input()
left = string[:len(string)//2]
right = string[len(string)//2:]
rotate_left = 0
rotate_right = 0
for char in left:
    rotate_left += ord(char) - 65
for char in right:
    rotate_right += ord(char) - 65
rotated_left = ""
rotated_right = ""
for char in left:
    rotated_left += chr(65 + (ord(char) - 65 + rotate_left)%26)
for char in right:
    rotated_right += chr(65 + (ord(char) - 65 + rotate_right)%26)
res = ""
for i in range(len(rotated_right)):
    res += chr(65 + (ord(rotated_left[i]) - 65 + ord(rotated_right[i]) - 65) % 26)
print(res)