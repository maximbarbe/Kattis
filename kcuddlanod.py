first, sec = input().split(" ")
first = [char for char in first]
sec = [char for char in sec]
for i in range(len(first)):
    if first[i] == "2":
        first[i] = "5"
    elif first[i] == "5":
        first[i] = "2"
for i in range(len(sec)):
    if sec[i] == "2":
        sec[i] = "5"
    elif sec[i] == "5":
        sec[i] = "2"
first = int("".join(first[::-1]))
sec = int("".join(sec[::-1]))
print(1 if first > sec else 2)