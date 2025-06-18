string = input()
initial = string[0]
up = 0
down = 0
like = 0
# like
for i in range(len(string) - 1):
    if string[i] != string[i + 1]:
        like += 1
        
prev = initial
#up
for i in range(1, len(string)):
    if prev == "D" and string[i] == "D":
        up += 1
        prev = "U"
    elif prev == "D" and string[i] == "U":
        up += 1
        prev = "U"
    elif prev == "U" and string[i] == "D":
        up += 2
        prev = "U"
#down
prev = initial
for i in range(1, len(string)):
    if prev == "U" and string[i] == "U":
        down += 1
        prev = "D"
    elif prev == "U" and string[i] == "D":
        down += 1
        prev = "D"
    elif prev == "D" and string[i] == "U":
        down += 2
        prev = "D"
        
print(up)
print(down)
print(like)