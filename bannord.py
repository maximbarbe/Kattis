s = input()
data = input().split(" ")
for i in range(len(data)):
    for char in s:
        if char in data[i]:
            data[i] = "*" * len(data[i])
print(" ".join(data))