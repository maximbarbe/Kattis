string = input()
left = 0
right = 0
i = 0
while string[i] != "(":
    left += 1
    i += 1
i += 1
while i != len(string) - 1:
    right += 1
    i += 1
if left == right:
    print("correct")
else:
    print("fix")